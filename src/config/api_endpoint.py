from config.configs import Configs


class ApiEndpoint:
    # Load API base URL from environment variable
    BASE_URL = Configs.apiUrl

    # Define endpoints
    PREDICT_BOTTLE = f"{BASE_URL}/processImageBottle"
    PREDICT_CAN = f"{BASE_URL}/processImageCan"
