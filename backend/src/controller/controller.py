# Controls the flow of the whole of the back-end
from backend.src.controller import recipe, utils, ManageThread
from queue import Queue
import threading
import json
import os
from controller import recipe


class Controller:
    def __init__(self):
        self.current_recipe = None
        self.thread_instance = None

    def new_recipe(self, recipe_id):
        self.current_recipe = recipe.Recipe(recipe_id)
        self.thread_instance = ManageThread(
            self.get_progression_requirements_for_current_step
        )

    def get_command_for_step(self, step_number):
        return self.current_recipe.get_command_for_step(step_number)

    def get_command_for_current_step(self):
        return self.current_recipe.get_command_for_current_step()

    def get_progression_requirements_for_step(self, step_number):
        return self.current_recipe.get_progression_requirements_for_step(step_number)

    def get_progression_requirements_for_current_step(self):
        return self.current_recipe.get_progression_requirements_for_current_step()

    def get_recipe_metadata(self):
        return self.current_recipe.get_recipe_metadata()


    def progress_next_step(self):
        self.current_recipe.increment_step()
        self.thread_instance.progress_next_step(
            self.get_progression_requirements_for_current_step
        )
        # Notify frontend

    def get_all_recipe_metadata(self):
        recipes = utils.get_json(utils.get_database_address("Recipes")).get(
            "recipes", []
        )
        all_metadata = [
            {
                "image": recipe.get("image", ""),
                "name": recipe.get("name", ""),
                "description": recipe.get("description", ""),
            }
            for recipe in recipes
        ]
        return all_metadata


CONTROLLER_INSTANCE = Controller()


##while True:
##    if CONTROLLER_INSTANCE.get_detection_listener_state():
##        CONTROLLER_INSTANCE.progress_next_step()
"""
import interpreter
from queue import Queue
import threading


def consumer(inters):
    inters.detection_loop()


recipe_queue = Queue()
inter = interpreter.Interpreter(recipe_queue)
recipe_queue.put(["prep", "Red-Onion", "chopped-Red-Onion"])
t1 = threading.Thread(
    target=consumer,
    args=(inter, )
)

t1.start()

while True:
    if inter.get_detection_listener_state():
        print("put in new next step")
        inter.put_new_step_into_queue(["prep", "Chopped-Red-Onion", "Red-Onion"])
        inter.Detection_listener.clear()

"""

CONTROLLER_INSTANCE.new_recipe(1)
