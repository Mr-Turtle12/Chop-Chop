# How to call:
# Initialize the object:
# detector = ObjectDetection.ObjectDetection("./Database/best.pt", 0)

# To check for a food item, e.g., "onion":
# detector.check_items("onion")
# return:
# [False]

# To check for more than one food item, e.g., "onion" and "carrot":
# detector.check_items(["onion", "carrot"])
# return:
# [False,False]

# Once all detecting have finished:
# detector.end()


from objectDetection import detection
from objectDetection import camera


class ObjectDetection:
    def __init__(self, model, cameraID):
        self.AI = detection.Detection(model)
        self.cameraObj = camera.Camera([1280, 720], cameraID)

    # Will set everything up to check the frame for any objects that is passed in to it
    def check_items(self, items):
        #This is called twice because the first time, sometimes the camera doesn't capture anything, so running it twice ensures that the frame from the camera is captured."
        _, frame = self.cameraObj.cap.read()
        _, frame = self.cameraObj.cap.read()
        self.cameraObj.show(frame)
        return self.AI.process_frame(frame, items)

    # To be called at the end

    def end(self):
        self.cameraObj.release()
