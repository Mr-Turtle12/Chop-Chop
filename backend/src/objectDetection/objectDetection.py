# How to call:
# Initialize the object:
# detectorObj = objectDetection.ObjectDetection("./Trained-Data/Version3/runs/detect/train/weights/best.pt", 0)

# To check for a food item, e.g., "Red-Onion":
# detectorObj.check_items("Red-Onion")
# return:
# [False]

# To check for more than one food item, e.g., "Red-Onion" and "carrot":
# detectorObj.check_items(["Red-Onion", "carrot"])
# return:
# [False,False]

# Once all detecting have finished:
# detector.end()

import time

from backend.src import config
from backend.src.objectDetection import detection
from backend.src.objectDetection import camera



class ObjectDetection:
    def __init__(self, camera_id):
        self.AI = detection.Detection(
            config.MODEL_LOCATION, config.CONFIDENCE_THRESHOLD
        )
        self.cameraObj = camera.Camera([1280, 720], camera_id)

    # Will set everything up to check the frame for any objects that is passed in to it
    def check_items(self, progression_object, inhibitor):
        # wait 1 seconds to give camera time to load up
        _, frame = self.cameraObj.cap.read()
        self.cameraObj.show(frame)
        return self.AI.process_frame(frame, progression_object, inhibitor)

    # To be called at the end

    def end(self):
        self.cameraObj.release()
