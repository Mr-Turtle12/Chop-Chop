from backend.src import objectDetection
from backend.src import config
from backend.src.utils import utils


# Set up global camera objects
PREP_CAMERA = None
COOK_CAMERA = None


class InvalidCamera(Exception):
    """Create a class to throw an error when there isn't a camera initialize"""

    "Camera not created"
    pass


def detection_loop(current_step, flag, cameras):
    """Runs the detection loop until the majority of frame return true, both number of frame and the number that need to be true are set in config.py.
    Args:
        current_step (tuple): A tuple containing information about the current step in the formate [camera, progression_object, inhibitor].
    """
    rolling_average = utils.LimitedQueue()
    while True:
        if flag.is_set():
            break
        rolling_average.append(check_step(current_step, cameras))
        if rolling_average.get_average():
            break


def check_step(current_step, cameras):
    """Checks the current step based on the provided parameters.
    Args:
        current_step (list): A list containing information about the current step.
    Returns:
        bool: Returns a boolean value indicating the result of the check.
    """
    prep_camera = cameras[0]
    cook_camera = cameras[1]
    progression_object = current_step[1]
    inhibitor = [current_step[2], "hand"]
    if current_step[0] == "cook":
        if cook_camera is not None:
            return cook_camera.check_items(progression_object, inhibitor)
        else:
            raise InvalidCamera
    else:
        if prep_camera is not None:
            return prep_camera.check_items(progression_object, inhibitor)
        else:
            raise InvalidCamera


def create_camera():
    """Creates camera objects based on the configuration."""
    if len(config.CAMERA_IDS) > 1:
        prep_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
        cook_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[1])
    elif len(config.CAMERA_IDS) > 0:
        prep_camera = objectDetection.ObjectDetection(config.CAMERA_IDS[0])
        cook_camera = None
    else:
        raise InvalidCamera
    return [prep_camera, cook_camera]


def destroy_camera(cameras):
    """Destroys camera objects if they exist."""
    if cameras[1] is not None:
        cameras[1].end()
    if cameras[0] is not None:
        cameras[0].end()
