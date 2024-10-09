from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/processImageCan", methods=["POST"])
def process_image_can():
    try:
        print(f"Request: {request.files}")

        # Check if the request contains a file
        if "imageFile" not in request.files:
            return jsonify({"error": "Invalid image file"}), 400

        image_file = request.files["imageFile"]
        print(f"image_file: {image_file}")

        # Simulate image processing (this would be where model processing happens)
        # Example: checking the file format, model predictions, etc.
        if not image_file.filename.lower().endswith(("png", "jpg", "jpeg")):
            return jsonify({"error": "Invalid image file"}), 400

        # Dummy logic to simulate model's detection and error cases
        # Simulate different cases:
        # - Found more than one object
        # - No object found
        # - Object in wrong field
        # - Valid can detected
        detection_result = simulate_model_detection(image_file)

        if detection_result == "multiple_objects":
            return jsonify({"error": "The user has inserted more than one object"}), 404
        elif detection_result == "no_detection":
            return jsonify({"error": "No detection found"}), 404
        elif detection_result == "wrong_object":
            return (
                jsonify(
                    {"error": "The user has inserted the object into the wrong field"}
                ),
                404,
            )
        elif detection_result == "500":
            return jsonify({"error": "Internal server error"}), 500
        elif detection_result == "400":
            return jsonify({"error": "Bad request"}), 400
        else:
            response_data = {
                "isValidCan": True,
                "brand": "pepsi",
                "size": 325,
                "confidence": 0.98,
            }
            return jsonify(response_data), 200

    except Exception as e:
        # Handle any internal server errors
        return jsonify({"error": "Internal server error"}), 500


# Dummy function to simulate model detection
def simulate_model_detection(image_file):
    # return "valid"  # 200
    # return "500"  # 500
    return "400"  # 400
    # return "no_detection"  # 404
    # return "multiple_objects"  # 404
    # return "wrong_object"       # 404


if __name__ == "__main__":
    app.run(debug=True)
