import cv2
import numpy as np

# Get the frame from camera

class Camera:
    def __init__(self, resolution, camera_ID):
        # Set up the camera
        self.frame_width, self.frame_height = resolution
        self.cap = cv2.VideoCapture(camera_ID)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

    def show(self, frame):
        cv2.imshow("yolov8", frame)
        cv2.waitKey(1)


    def release(self):
        self.cap.release()