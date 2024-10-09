from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


class Configs:
    firmwareVersion = os.getenv("FIRMWARE_VERSION")
    modelVersion = os.getenv("MODEL_VERSION")

    apiUrl = os.getenv("API_URL")

    mqttBroker = os.getenv("MQTT_BROKER")
    mqttPort = int(os.getenv("MQTT_PORT"))
    mqttClientId = os.getenv("MQTT_CLIENT_ID")
    mqttUser = os.getenv("MQTT_USER")
    mqttPassword = os.getenv("MQTT_PASSWORD")

    mqttSubscribeTopic = os.getenv("MQTT_SUB_TOPIC")
    mqttPublishTopic = os.getenv("MQTT_PUB_TOPIC")

    camBottle = int(os.getenv("CAM_BOTTLE"))
    camCan = int(os.getenv("CAM_CAN"))
    frameSkip = int(os.getenv("FRAME_SKIP"))
