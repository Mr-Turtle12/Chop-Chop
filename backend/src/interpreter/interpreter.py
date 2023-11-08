from backend.src import objectDetection
from backend.src import config
from backend.src.controller import utils


# Set up global camera objects
PREP_CAMERA = None
COOK_CAMERA = None


def detection_loop(current_step):
    """Runs the detection loop until the the majority of frame return true, both number of frame and the number that need to be true are set in config.py.
    Args:
        current_step (tuple): A tuple containing information about the current step in the formate [camera, progression_object, inhibitor].
    """
    create_camera()
    rolling_average = utils.LimitedQueue()
    while True:
        rolling_average.append(check_step(current_step))
        print(rolling_average.get_average())
        if rolling_average.get_average():
            break
    destroy_camera()


def check_step(current_step):
    """Checks the current step based on the provided parameters.
    Args:
        current_step (list): A list containing information about the current step.
    Returns:
        bool: Returns a boolean value indicating the result of the check.
    """
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
    """Creates camera objects based on the configuration."""
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
    """Destroys camera objects if they exist."""
    global PREP_CAMERA
    global COOK_CAMERA
    if COOK_CAMERA is not None:
        COOK_CAMERA.end()
    if PREP_CAMERA is not None:
        PREP_CAMERA.end()
