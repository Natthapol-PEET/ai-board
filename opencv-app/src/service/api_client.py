import time
import requests

from config.api_endpoint import ApiEndpoint
from config.predictions import PredictionType
from helper.log_flight import LogFlight


class ApiClient:
    def __init__(self, mock_image=False, mock_response=None):
        self.mock_image = mock_image
        self.mock_response = mock_response

    def get_url(self, prediction_type):
        if prediction_type == PredictionType.can:
            return ApiEndpoint.PREDICT_CAN
        return ApiEndpoint.PREDICT_BOTTLE

    def get_mock_image(self, prediction_type):
        if prediction_type == PredictionType.can:
            return "src/image/can.jpg"
        return "src/image/bottle.jpg"

    def get_image(self, prediction_type):
        if prediction_type == PredictionType.can:
            return "can.jpg"
        return "bottle.jpg"

    def predict_image(self, prediction_type=None, image_file_path=None):
        endpoint_url = self.get_url(prediction_type)

        LogFlight.info(f"image_file_path: {image_file_path}")
        image_path = image_file_path

        if image_file_path is None:
            if self.mock_image:
                image_path = self.get_mock_image(prediction_type)
            else:
                image_path = self.get_image(prediction_type)
        LogFlight.info(f"image_path: {image_path}")

        files = {
            "file": open(image_path, "rb"),
        }

        # with open(image_path, "rb") as f:
        #     files = {"file": f}
        #     LogFlight.info(files)
 
        response = self.post_with_retries(endpoint_url, files)
        if isinstance(response, Exception):
            return response

        # response = requests.post(endpoint_url, files=files, timeout=120)
        LogFlight.warning(f"Response code: {response.status_code}")
        LogFlight.warning(f"Response text: {response.text}")
        return response

    def post_with_retries(self, url, files, max_retries=3, delay=5):
        for attempt in range(max_retries):
            try:
                response = requests.post(url, files=files)
                return response
            except (requests.RequestException, BrokenPipeError) as e:
                if attempt < max_retries - 1:
                    time.sleep(delay)
                    continue
                LogFlight.warning(f"Request failed: {e}")
                return e
