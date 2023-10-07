from controller import utils


class Recipe:
    def __init__(self, recipe_id):
        # self.current_recipe = utils.get_JSON(utils.get_database_address(recipe_name))
        self.current_step = 1

    def get_current_step(self):
        return self.current_step

    ##Get current step json data

    ## Go forward step

    ## Go back step
