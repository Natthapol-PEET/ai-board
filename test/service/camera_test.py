from service.camera import CameraCapture
import argparse


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Camera Capture Script")
    parser.add_argument("camera_index", type=int, help="Index of the camera to use")

    # Parse arguments
    args = parser.parse_args()

    # Pass the camera_index from the arguments
    camera = CameraCapture(camera_index=args.camera_index)
    camera.show_video()

    # camera.save_frame("test.jpg")
    # camera.release_camera()
