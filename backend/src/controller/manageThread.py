from backend.src.interpreter import interpreter
from backend.src.controller import controller
from backend.src.utils import utils


class ManageThread:
    """Class to manage threads for interpreting steps."""

    def __init__(self, current_step, flag, cameras):
        self.interpreter_instance = None
        self.thread = None
        self.init_interpreter_thread(current_step, flag, cameras)

    def init_interpreter_thread(self, current_step, flag, cameras):
        """Initializes the interpreter thread for the current step.
        Args:
            current_step (object): The current step object.
        """
        thread = utils.BaseThread(
            name="StepJob",
            target=lambda: (interpreter.detection_loop(current_step, flag, cameras)),
            callback=self.end_thread,
            callback_args=(
                flag,
                cameras,
            ),
        )
        thread.start()

    def end_thread(self, flag, cameras):
        if not flag.is_set():
            controller.CONTROLLER_INSTANCE.progress_next_step()
        else:
            interpreter.destroy_camera(cameras)
            flag.clear()
