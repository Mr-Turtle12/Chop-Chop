import cv2
import numpy as np

#Get the Frame from camare 
class getCamare:
    def __init__(self, resolution,camareID):
        #Set up the camare
        self.frame_width, self.frame_height = resolution
        self.cap = cv2.VideoCapture(camareID)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

    def release(self):
        self.cap.release()
