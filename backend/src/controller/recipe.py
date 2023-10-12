from controller import utils


class Recipe:
    def __init__(self, recipe_id):
        self.current_recipe = utils.fetch_recipe_by_id(recipe_id, utils.get_JSON(utils.get_database_address("QSBRecipe.json")))
        self.current_step = 1

    def get_current_step(self):
        return self.current_step

    def get_command_for_step(self, step_number):
        if self.current_recipe:
            steps = self.current_recipe.get('steps', [])
            if 1 <= step_number <= len(steps):
                return steps[step_number - 1].get('command', '')
        return None

    def get_command_for_current_step(self):
        return self.get_command_for_step(self.current_step)

    ##Get current step json data

    ## Go forward step

    ## Go back step
