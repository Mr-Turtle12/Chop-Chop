from backend.src import objectDetection
from backend.src import config
from backend.src.controller import utils


class InvalidCamera(Exception):
    """Create a class to throw an error when there isn't a camera initialize"""

    "Camera not created"
    pass


def detection_loop(prep_camera, cook_camera, current_step):
    """Runs the detection loop until the majority of frame return true, both number of frame and the number that need to be true are set in config.py.
    Args:
        current_step (tuple): A tuple containing information about the current step in the formate [camera, progression_object, inhibitor].
    """
    rolling_average = utils.LimitedQueue()
    while True:
        rolling_average.append(check_step(prep_camera, cook_camera, current_step))
        if rolling_average.get_average():
            break


def check_step(prep_camera, cook_camera, current_step):
    """Checks the current step based on the provided parameters.
    Args:
        current_step (list): A list containing information about the current step.
    Returns:
        bool: Returns a boolean value indicating the result of the check.
    """
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
