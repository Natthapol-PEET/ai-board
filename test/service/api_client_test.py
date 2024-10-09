from config.api_endpoint import ApiEndpoint
from service.api_client import ApiClient


if __name__ == "__main__":
    # Usage
    client = ApiClient()

    image_file_path = "src/can.jpg"
    serial_number = "12345ABC"

    prediction_type = ApiEndpoint.PREDICT_BOTTLE
    response = client.predict_image(
        image_file_path=image_file_path,
        prediction_type=prediction_type,
    )

    # Print response
    print(response.status_code)
    print(response.text)
