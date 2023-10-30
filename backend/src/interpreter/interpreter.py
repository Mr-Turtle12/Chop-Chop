from backend.src import objectDetection
from backend.src import config
import threading


class Interpreter:
    def __init__(self, recipe_queue):
        # set up one or two cameras
        self.prep_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
        self.current_step = []
        if len(config.CAMERA_IDS) > 1:
            self.cook_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[1])
        self.recipe_queue = recipe_queue
        self.Detection_listener = threading.Event()

    # This loop will do run in another thread and will get the current step passed into it via the queue and set an
    # event once the step has been detected
    def detection_loop(self):
        while True:
            print(self.current_step)
            if not self.recipe_queue.empty():
                self.current_step = self.recipe_queue.get()
            if self.current_step:
                if self.check_step():
                    self.Detection_listener.set()

    def get_detection_listener_state(self):
        return self.Detection_listener.is_set()

    def put_new_step_into_queue(self, step):
        self.recipe_queue.put(step)

    # Pass into from json the camera name and the objects you want to check e.g [camera, progressionObject , inhibitor]
    def check_step(self):
        progressionObject = self.current_step[1]
        inhibitor = [self.current_step[2], "hand"]
        if self.current_step[0] == "cook":
            return self.cook_camera.check_items(progressionObject, inhibitor)
        else:
            return self.prep_camera.check_items(progressionObject, inhibitor)
