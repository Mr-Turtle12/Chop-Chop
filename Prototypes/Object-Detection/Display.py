import cv2
import numpy as np

#Display class is for all the setting and displaying cv2 window with text
class Display:
    def __init__(self, resolution):
        self.frame_width, self.frame_height = resolution
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
        self.font_scale = 1
        self.font_color = (255, 255, 255)
        self.font_thickness = 2
        self.font_face = cv2.FONT_HERSHEY_SIMPLEX
        self.image = np.zeros((self.frame_height, self.frame_width, 3), dtype=np.uint8)

    def set_text(self, text):
        position = (100, 200)
        self.image = np.zeros((self.frame_height, self.frame_width, 3), dtype=np.uint8)
        cv2.putText(self.image, text, position, self.font_face, self.font_scale, self.font_color, self.font_thickness)

    def show_image(self):
        cv2.imshow("Image with Text", self.image)
    def Breakloop(self):
        if cv2.waitKey(30) == 27:
            return True

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()


