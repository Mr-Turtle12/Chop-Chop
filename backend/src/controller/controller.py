# Controls the flow of the whole of the back-end

from controller import recipe
from controller import utils


class Controller:
    def __init__(self):
        self.current_recipe_instance = None

    # Get the required recipe from the JSON files
    # Begin incrementing the steps.
    def new_recipe(self, recipe_id):
        if utils.does_recipe_id_exist(recipe_id):
            self.current_recipe_instance = recipe.Recipe(recipe_id)
            return True
        else:
            return False

    def get_all_recipe_metadata():
        print("Get all Recipe metadata")
        # Returns information about all recipes (as dictionary)
        # `recipe_name`,`recipe_picture`, `recipe_description`  (if possible)

    def get_a_recipe(recipe_id):
        print("Get Recipe information")

    def get_current_recipe_step(self):
        if self.current_recipe_instance is not None:
            return self.current_recipe_instance.get_current_step()
        return -1

    # returns the informations about a specific recipe


def test_new_recipe():
    CONTROLLER_INSTANCE.new_recipe("DemoRecipe")


CONTROLLER_INSTANCE = Controller()
