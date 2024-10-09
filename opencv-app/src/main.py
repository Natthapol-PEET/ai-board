import ast
import time
from config.configs import Configs
from config.globals import Globals, clear_globals
from helper.log_flight import LogFlight
from model.ack_response import AckResponse
from model.boot_notification import BootNotification
from model.heardbeat import Heardbeat
from model.request_start_transaction import RequestStartTransaction
from model.transaction_event import TransactionEvent
from service.api_client import ApiClient
from service.camera import CameraCapture
from service.mqtt_client import MQTTClient
import threading

# Initialize logging
LogFlight.initialize()

apiClient = ApiClient(mock_image=False)


def on_event_update():
    # TransactionEvent  Started
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        TransactionEvent(
            id=Globals.transactionId,
            status="Started",
        ),
        qos=2,
    )

    # TransactionEvent  Updated
    # start camera
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        TransactionEvent(
            id=Globals.transactionId,
            status="Updated",
            data={
                "detail": "StartCameraCapture",
                "camera_index": (
                    Configs.camCan if Globals.objectType == "can" else Configs.camBottle
                ),
                "camera_detail": Globals.objectType,
            },
        ),
        qos=2,
    )

    try:
        camera = CameraCapture(prediction_type=Globals.objectType)
        camera.save_frame(f"{Globals.objectType}.jpg")
        camera.release_camera()
    except Exception as e:
        LogFlight.error(e)
        mqtt_client.publish(
            Configs.mqttPublishTopic,
            AckResponse(
                id=Globals.transactionId,
                status=False,
                reason=str(e.message) if hasattr(e, "message") else str(e),
            ),
            qos=2,
        )

        clear_globals()
        return

    # stop camera
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        TransactionEvent(
            id=Globals.transactionId,
            status="Updated",
            data={"detail": "StopCameraCapture"},
        ),
        qos=2,
    )

    # start predict
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        TransactionEvent(
            id=Globals.transactionId,
            status="Updated",
            data={"detail": "StartPrediction"},
        ),
        qos=2,
    )

    try:
        resp = apiClient.predict_image(
            image_file_path=None,
            prediction_type=Globals.objectType,
        )
    except Exception:
        LogFlight.error(e)

        mqtt_client.publish(
            Configs.mqttPublishTopic,
            AckResponse(
                id=Globals.transactionId,
                status=False,
                reason=str(e.message) if hasattr(e, "message") else str(e),
            ),
            qos=2,
        )

        clear_globals()
        return

    # stop predict
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        TransactionEvent(
            id=Globals.transactionId,
            status="Updated",
            data={"detail": "StopPrediction"},
        ),
        qos=2,
    )

    # TransactionEvent  Ended
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        TransactionEvent(
            id=Globals.transactionId,
            status="Ended",
            data={
                "detail": "SummarizeResult",
                "result": {
                    "status": resp.status_code,
                    "data": resp.json(),
                    # "data": {
                    #     "isValidBottle": True,
                    #     "brand": "oishi",
                    #     "size": 500,
                    #     "confidence": 0.89,
                    # },
                },
            },
        ),
        qos=2,
    )

    # Clear Globals
    clear_globals()


def on_message(client, userdata, msg):
    try:
        LogFlight.info(f"Message received: {msg.topic} {msg.payload}")
        payload = ast.literal_eval(msg.payload.decode("utf-8"))

        if payload["event"] == "RequestStartTransaction":
            try:
                RequestStartTransaction(**payload)

                if Globals.transactionId is not None:
                    return mqtt_client.publish(
                        Configs.mqttPublishTopic,
                        AckResponse(
                            id=Globals.transactionId,
                            status=False,
                            reason="Transaction Processing",
                        ),
                        qos=2,
                    )

                # Set Globals
                Globals.transactionId = payload["id"]
                Globals.objectType = payload["data"]["type"]
                Globals.serialNumber = payload["data"]["serial"]

                mqtt_client.publish(
                    Configs.mqttPublishTopic,
                    AckResponse(
                        id=Globals.transactionId,
                        status=True,
                    ),
                    qos=2,
                )

                thread = threading.Thread(target=on_event_update)
                thread.start()
            except Exception as e:
                LogFlight.error(e)
                mqtt_client.publish(
                    Configs.mqttPublishTopic,
                    AckResponse(
                        id=Globals.transactionId,
                        status=False,
                        reason="Invalid Data",
                    ),
                    qos=2,
                )

        elif payload["event"] == "GetLog":
            return mqtt_client.publish(
                Configs.mqttPublishTopic,
                AckResponse(
                    id=payload["id"],
                    status=True,
                    reason=LogFlight.get_log(),
                ),
                qos=2,
            )
        else:
            mqtt_client.publish(
                Configs.mqttPublishTopic,
                AckResponse(
                    id=Globals.transactionId,
                    status=False,
                    reason="Unknown event",
                ),
                qos=2,
            )

    except Exception as e:
        LogFlight.error(e)
        mqtt_client.publish(
            Configs.mqttPublishTopic,
            AckResponse(
                id=Globals.transactionId,
                status=False,
                reason=f"Error: {e}",
            ),
            qos=2,
        )


if __name__ == "__main__":
    global mqtt_client

    mqtt_client = MQTTClient(
        broker=Configs.mqttBroker,
        port=Configs.mqttPort,
        client_id=Configs.mqttClientId,
        username=Configs.mqttUser,
        password=Configs.mqttPassword,
        on_message=on_message,
    )
    mqtt_client.connect()
    mqtt_client.loop_start()

    ## BootNotification message
    mqtt_client.publish(
        Configs.mqttPublishTopic,
        BootNotification(Configs.firmwareVersion, Configs.modelVersion),
        qos=2,
        retain=True,
    )

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
