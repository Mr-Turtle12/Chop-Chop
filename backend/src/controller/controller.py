import json
from backend.src.controller import recipe, utils, manageThread


class Controller:
    """Controls the flow of the whole backend system."""

    def __init__(self):
        self.current_recipe = None
        self.thread_instance = None
        self.step_changed_flag = utils.StepChangeFlag()

    def new_recipe(self, recipe_id):
        """Starts a new recipe with the given recipe ID.
        Args:
            recipe_id (int): The ID of the recipe to start.
        """
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

    def get_recipe_metadata(self, recipe_id):
        recipes = utils.get_json(utils.get_database_address("Recipes")).get(
            "recipes", []
        )
        recipe = utils.fetch_recipe_by_id(recipe_id, recipes)
        metadata = {
            "image": recipe.get("image", ""),
            "name": recipe.get("name", ""),
            "description": recipe.get("description", ""),
            "ingredients": recipe.get("ingredients", []),
            "commands": [],
        }
        for step_num in range(1, len(metadata["steps"])):
            command = self.get_command_for_step(step_num)
            metadata["commands"].append(json.loads(command))
        return json.dumps(metadata)

    def progress_next_step(self):
        """Progresses to the next step in the recipe."""
        self.current_recipe.increment_step()
        self.thread_instance = manageThread.ManageThread(
            self.get_progression_requirements_for_current_step()
        )
        self.step_changed_flag.state = True
        # Notify frontend

    def get_all_recipe_metadata(self):
        """Gets metadata for all recipes.
        Returns:
            list: A list of dictionaries containing metadata for all recipes.
        """
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
        return json.dumps(all_metadata)


# start a instance for the controller
CONTROLLER_INSTANCE = Controller()
