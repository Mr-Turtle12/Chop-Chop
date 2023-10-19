# Controls the flow of the whole of the back-end
from backend.src.controller import recipe, utils


class Controller:
    def __init__(self):
        self.current_recipe = None

    def new_recipe(self, recipe_id):
        self.current_recipe = recipe.Recipe(recipe_id)

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

    def get_all_recipe_metadata(self):
        all_metadata = []

        for recipe in utils.get_json(utils.get_database_address("Recipes")).get('recipes', []):
            metadata = {
                'image': recipe.get('image', ''),
                'name': recipe.get('name', ''),
                'description': recipe.get('description', ''),
            }
            all_metadata.append(metadata)

        return all_metadata


def test_new_recipe():
    recipe_id = "1"
    CONTROLLER_INSTANCE.new_recipe(recipe_id)
    print(CONTROLLER_INSTANCE.get_command_for_step(1))
    print(CONTROLLER_INSTANCE.get_progression_requirements_for_current_step())
    print(CONTROLLER_INSTANCE.get_all_recipe_metadata())

CONTROLLER_INSTANCE = Controller()
