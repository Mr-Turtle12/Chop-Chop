# Controls the flow of the whole of the back-end
import os
from backend.controller import utils
from backend.controller import recipe


class Controller:
    def __init__(self):
        self.current_recipe_instance = {}

    # Get the required recipe from the JSON files
    # Begin incrementing the steps.
    def new_recipe(self, recipe_name):
        self.current_recipe_instance = recipe.Recipe(recipe_name)


def test_print():
    print("Hello")
