from queue import Queue
import threading
from backend.src.interpreter import interpreter


class createThread:
    def __init__(self, current_step):
        self.interpreter_instance = None
        self.recipe_queue = Queue()
        self.thread = None
        self.init_interpreter_thread(current_step)

    def run_interpreter(self, interpreter):
        interpreter.detection_loop()

    def init_interpreter_thread(self, current_step):
        self.recipe_queue.put(current_step)
        interpreter_instance = interpreter.Interpreter(self.recipe_queue)
        self.thread = threading.Thread(
            target=self.run_interpreter, args=(interpreter_instance)
        )
        self.thread.start()

    def progress_next_step(self, get_progression_requirements_for_current_step):
        self.interpreter_instance.put_new_step_into_queue(
            get_progression_requirements_for_current_step
        )
        self.interpreter_instance.Detection_listener.clear()

    def get_detection_listener_state(self):
        if self.interpreter_instance != None:
            return self.interpreter_instance.get_detection_listener_state()
        else:
            return False

    def end_thread(self):
        self.thread.exit()
        self.recipe_queue.clear()
