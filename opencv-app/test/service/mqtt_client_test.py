from config.configs import Configs
from service.mqtt_client import MQTTClient


if __name__ == "__main__":
    mqtt_client = MQTTClient(
        broker=Configs.mqttBroker,
        port=Configs.mqttPort,
        client_id=Configs.mqttClientId,
        username=Configs.mqttUser,
        password=Configs.mqttPassword,
    )
    mqtt_client.connect()
    mqtt_client.loop_start()

    mqtt_client.subscribe(Configs.mqttSubscribeTopic)

    # Publishing a test message
    mqtt_client.publish(Configs.mqttPublishTopic, "Hello MQTT!", qos=2)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    finally:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
