# source
# https://github.com/Mabelzzz/AI_Project/blob/main/main.py
from ultralytics import YOLO


class Prediction:
    def __init__(self):
        self.model = YOLO("src/weights/best4.pt")

    def run_model(self, image_path):
        results = self.model(image_path)
        # results[0].show()

        return results

    def check_detection(self, results):
        if len(results[0].boxes) == 0:  # No detections found in the image
            return False
        return True

    def check_item(self, item, items_model):
        print(f"Item: {item}, Model: {items_model}")
        if item == "bottle" and items_model == "GreenTech-bottle":
            return True
        if item == "can" and items_model == "GreenTech-can":
            return True
        return False

    def process(self, item, filename):
        try:
            # Run the model on the image based on the item
            results = self.run_model(filename)
            print(f"Results: {results}")

            # Check if the image can be classified
            if not self.check_detection(results):
                raise Exception("No detection found")

            # If the image is valid, classify it
            if len(results[0].boxes) > 0 and hasattr(results[0], "boxes"):
                is_valid_obj = True
                confidence = None
                items_model = None

                for detection in results[0].boxes:
                    confidence = float(detection.conf.numpy())  # Ensure this is a float
                    cls = int(detection.cls.numpy())  # Ensure this is an integer
                    items_model = self.model.names.get(
                        cls, "Unknown"
                    )  # Safely access class name
                    print(f"Class: {items_model}, Confidence: {confidence}")

                is_valid_obj = self.check_item(item, items_model)
                print(f"Valid: {is_valid_obj}")

                return (
                    {"isValidCan": is_valid_obj, "confidence": confidence}
                    if item == "can"
                    else {"isValidBottle": is_valid_obj, "confidence": confidence}
                )

            return results
        except Exception as e:
            raise e
