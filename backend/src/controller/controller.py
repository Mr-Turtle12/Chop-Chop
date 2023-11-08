# Controls the flow of the whole of the back-end
from backend.src.controller import recipe, utils, manageThread
from queue import Queue
import threading
import json
import os


class Controller:
    def __init__(self):
        self.current_recipe = None
        self.thread_instance = None

    def new_recipe(self, recipe_id):
        self.current_recipe = recipe.Recipe(recipe_id)
        self.thread_instance = manageThread.ManageThread(
            self.get_progression_requirements_for_current_step()
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
        print("next step")
        self.current_recipe.increment_step()
        self.thread_instance = manageThread.ManageThread(
            self.get_progression_requirements_for_current_step()
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
