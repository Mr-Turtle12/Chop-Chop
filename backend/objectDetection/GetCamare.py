import cv2
import numpy as np

# Get the frame from camare


class GetCamare:
    def __init__(self, resolution, camare_ID):
        # Set up the camare
        self.frame_width, self.frame_height = resolution
        self.cap = cv2.VideoCapture(camare_ID)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

    def show(self, frame):
        cv2.imshow("yolov8", frame)

    def release(self):
        self.cap.release()
