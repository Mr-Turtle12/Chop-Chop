# Controls the flow of the whole of the back-end

from controller import recipe


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

    def get_all_recipe_metadata(self):
        return "replace me"
        # Returns information about all recipes (as dictionary)
        # `recipe_name`,`recipe_picture`, `recipe_description`  (if possible)

    def get_a_recipe(self, recipe_id):
        return "replace me"
        # Return information about one singular recipe.
        # search by id and return, recipe_name, recipe_description, recipe_picture, recipe_steps, recipe_ingredients

    def get_current_recipe_step(self):
        # returns the current recipe step
        if self.current_recipe_instance is not None:
            return self.current_recipe_instance.get_current_step()
        return -1


def test_new_recipe():
    CONTROLLER_INSTANCE.new_recipe("DemoRecipe")


CONTROLLER_INSTANCE = Controller()
