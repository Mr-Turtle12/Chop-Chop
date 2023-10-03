from backend.controller import utils


class Recipe:
    def __init__(self, recipe_name):
        self.current_recipe = utils.get_JSON(utils.get_database_address(recipe_name))
        self.current_step = 1
