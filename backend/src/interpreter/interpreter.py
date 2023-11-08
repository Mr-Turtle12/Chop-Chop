from backend.src import objectDetection
from backend.src import config
import threading

PREP_CAMERA = None
COOK_CAMERA = None


class BaseThread(threading.Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')
        super(BaseThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self):
        self.method()
        if self.callback is not None:
            self.callback(*self.callback_args)


# This loop will do run in another thread and will get the current step passed into it via the queue and set an
# event once the step has been detected
def detection_loop(current_step):
    create_camera()
    while True:
        if check_step(current_step):
            break
    destroy_camera()


# Pass into from json the camera name and the objects you want to check e.g [camera, progressionObject , inhibitor]
def check_step(current_step):
    progression_object = current_step[1]
    inhibitor = [current_step[2], "hand"]
    if current_step[0] == "cook":
        if COOK_CAMERA is not None:
            return COOK_CAMERA.check_items(progression_object, inhibitor)
        else:
            print("ERROR COOK CAMERA NOT AVAILABLE ")
            return True
    else:
        if PREP_CAMERA is not None:
            return PREP_CAMERA.check_items(progression_object, inhibitor)
        else:
            print("ERROR PREP CAMERA NOT AVAILABLE ")
            return True


def create_camera():
    global PREP_CAMERA
    global COOK_CAMERA
    if len(config.CAMERA_IDS) > 1:
        PREP_CAMERA = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
        COOK_CAMERA = objectDetection.ObjectDetection(config.CAMERA_IDS[1])
    elif len(config.CAMERA_IDS) > 0:
        PREP_CAMERA = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
    else:
        print("ERROR PREP CAMERA NOT AVAILABLE ")

def destroy_camera():
    global PREP_CAMERA
    global COOK_CAMERA
    if COOK_CAMERA is not None:
        COOK_CAMERA.end()
    if PREP_CAMERA is not None:
        PREP_CAMERA.end()
