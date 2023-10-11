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
from objectDetection import detection
from objectDetection import camera


class ObjectDetection:
    def __init__(self, model, cameraID):
        self.AI = detection.Detection(model)
        self.cameraObj = camera.Camera([1280, 720], cameraID)

    # Will set everything up to check the frame for any objects that is passed in to it
    def check_items(self, items):
        #wait 1 seconds to give camera time to load up
        time.sleep(1)
        _, frame = self.cameraObj.cap.read()
        return self.AI.process_frame(frame, items)

    # To be called at the end

    def end(self):
        self.cameraObj.release()
