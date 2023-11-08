from backend.src import config
from backend.src.objectDetection import detection
from backend.src.objectDetection import camera


class ObjectDetection:
    def __init__(self, camera_id):
        """Initializes the ObjectDetection class.
        Args:
            camera_id (int): The ID of the camera.
        """
        self.AI = detection.Detection(
            config.MODEL_LOCATION, config.CONFIDENCE_THRESHOLD
        )
        self.cameraObj = camera.Camera([1280, 720], camera_id)

    def check_items(self, progression_object, inhibitor):
        """Checks the items in the current frame.
        Args:
            progression_object (str): The object to detect.
            inhibitor (list): A list of inhibitors.
        Returns:
            bool: True if the item is detected, otherwise False.
        """
        _, frame = self.cameraObj.cap.read()
        return self.AI.process_frame(frame, progression_object, inhibitor)

    def end(self):
        """Releases the camera object."""
        self.cameraObj.release()
