import objectDetection
import config


class Interpreter:
    def __init__(self):
        # set up Cameras depends if it's a one or two camera set up
        self.detect_prep = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
        if len(config.CAMERA_IDS) > 1:
            self.detect_cook = objectDetection.ObjectDetection(config.CAMERA_IDS[1])

    # Pass into from json the camera name and the objects you want to check e.g [progressionObject , inhibitor]
    def Check_Step(self, camera_name, object_array):
        object_array.append("Hands")
        if camera_name == "cook":
            return self.detect_cook.check_items(object_array) == [
                True,
                False,
                False,
            ]
        else:
            return self.detect_prep.check_items(object_array) == [
                True,
                False,
                False,
            ]
