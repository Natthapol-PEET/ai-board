import cv2

from config.configs import Configs
from config.predictions import PredictionType
from helper.log_flight import LogFlight


class CameraCapture:
    def __init__(self, prediction_type=None, camera_index=None):
        if camera_index is None:
            self.camera_index = self.get_camera_index(prediction_type)
        else:
            self.camera_index = camera_index

        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise ValueError(f"Cannot open camera with index {self.camera_index}")

    def get_camera_index(self, prediction_type):
        if prediction_type == PredictionType.can:
            return Configs.camCan
        return Configs.camBottle

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture image")

        return frame

    def show_video(self):
        while True:
            frame = self.capture_frame()
            cv2.imshow("Camera Feed", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def save_frame(self, file_path="captured_image.jpg"):
        for _ in range(Configs.frameSkip):
            frame = self.capture_frame()

        cv2.imwrite(file_path, frame)
        LogFlight.info(f"Image saved to {file_path}")

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
