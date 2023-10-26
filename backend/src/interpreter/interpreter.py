import objectDetection
import config


class Interpreter:
    def __init__(self):
        # set up Cameras depends if it's a one or two camera set up
        self.prep_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
        self.current_step = []
        if len(config.CAMERA_IDS) > 1:
            self.cook_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[1])

    # This loop will do run in another thread and will get the current step passed into it via the in_q and set a event once the step has been detected
    def detection_loop(self, in_q, event):
        while True:
            if in_q.empty():
                self.current_step = in_q.get()
                event.clear()
            # logic for when it's stir interrupt
            if self.check_step():
                event.set()

    # Pass into from json the camera name and the objects you want to check e.g [camera, progressionObject , inhibitor]
    def check_step(self):
        progressionObject = self.current_step[1]
        inhibitor = self.current_step[2]
        inhibitor.append("hand")
        if self.current_step[0] == "cook":
            return self.cook_camera.check_items(progressionObject, inhibitor)
        else:
            return self.prep_camera.check_items(progressionObject, inhibitor)
