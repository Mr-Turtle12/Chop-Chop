import cv2


class Camera:
    def __init__(self, resolution, camera_ID):
        """Initializes the Camera class.
        Args:
            resolution (list): A list containing the width and height of the camera resolution.
            camera_ID (int): The ID of the camera.
        """
        self.frame_width, self.frame_height = resolution
        self.cap = cv2.VideoCapture(camera_ID)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

    def show(self, frame):
        """Displays the frame.
        Args:
            frame (str): The frame to display.
        """
        cv2.imshow("yolov8", frame)
        cv2.waitKey(1)

    def release(self):
        """Releases the camera."""
        self.cap.release()
