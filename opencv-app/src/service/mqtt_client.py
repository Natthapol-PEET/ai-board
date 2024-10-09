import paho.mqtt.client as mqtt
from config.configs import Configs
from helper.log_flight import LogFlight


class MQTTClient:
    def __init__(
        self,
        broker,
        port=1883,
        client_id="",
        username=None,
        password=None,
        on_message=None,
    ):
        self.broker = broker
        self.port = port
        self.client_id = client_id or f"mqtt_client_{id(self)}"
        self.username = username
        self.password = password
        self.client = mqtt.Client(client_id=self.client_id)

        if self.username and self.password:
            self.client.username_pw_set(username=self.username, password=self.password)

        # Attach callbacks
        self.client.on_connect = self.on_connect
        # self.client.on_message = self.on_message
        self.client.on_message = on_message
        self.client.on_disconnect = self.on_disconnect

    def connect(self):
        self.client.connect(self.broker, self.port, keepalive=60)

        # Subscribe to topics
        self.topic_subscribe()

    def on_connect(self, client: mqtt.Client, userdata, flags, rc):
        LogFlight.info(f"Connected with result code {rc}")

    # def on_message(self, client, userdata, message):
    #     print(f"Message received: {message.topic} {message.payload}")

    def on_disconnect(self, client, userdata, rc):
        LogFlight.info("Disconnected")

    # def on_disconnect(self, client: mqtt.Client, userdata, rc):
    #     if rc != 0:
    #         print("Unexpected disconnection. Reconnecting...")
    #         client.reconnect()

    def subscribe(self, topic, qos=0):
        LogFlight.info(f"Subscribing: {topic}")
        self.client.subscribe(topic, qos=qos)

    def publish(self, topic, payload, qos=0, retain=False):
        LogFlight.info(f"Publishing: {topic} {payload.to_json()}")
        self.client.publish(
            topic=topic,
            payload=payload.to_json(),
            qos=qos,
            retain=retain,
        )

    def loop_start(self):
        self.client.loop_start()

    def loop_stop(self):
        self.client.loop_stop()

    def loop_forever(self):
        self.client.loop_forever()

    def disconnect(self):
        self.client.disconnect()

    def topic_subscribe(self):
        self.subscribe(Configs.mqttSubscribeTopic, qos=2)
