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

    def update_flag(self):
        self.step_changed_flag.state = True

    def get_command_for_step(self, step_number):
        return self.current_recipe.get_command_for_step(step_number)

    def get_command_for_current_step(self):
        return self.current_recipe.get_command_for_current_step()

    def get_progression_requirements_for_step(self, step_number):
        return self.current_recipe.get_progression_requirements_for_step(step_number)

    def get_progression_requirements_for_current_step(self):
        return self.current_recipe.get_progression_requirements_for_current_step()

    def get_recipe_metadata(self, recipe_id):
        # Fetch the recipes data from the JSON file
        recipes_data = utils.get_json(utils.get_database_address("Recipes"))
        recipes = recipes_data.get("recipes", [])

        # Find the specified recipe by its ID
        target_recipe = None
        for recipe in recipes:
            if int(recipe.get("id")) == recipe_id:
                target_recipe = recipe
                break

        if not target_recipe:
            return json.dumps({})  # Recipe not found, return an empty JSON object

        # Construct the metadata for the recipe
        metadata = {
            "image": target_recipe.get("image", ""),
            "name": target_recipe.get("name", ""),
            "description": target_recipe.get("description", ""),
            "ingredients": target_recipe.get("ingredients", []),
            "commands": [
                step.get("command", "") for step in target_recipe.get("steps", [])
            ],
        }

        return json.dumps(metadata)

    def progress_next_step(self):
        """Progresses to the next step in the recipe."""
        self.current_recipe.increment_step()
        self.thread_instance = manageThread.ManageThread(
            self.get_progression_requirements_for_current_step()
        )
        self.update_flag()
        # Notify frontend

    def set_step(self, step_numer):
        if self.current_recipe is not None:
            self.current_recipe.set_current_step(step_numer)
            self.thread_instance = manageThread.ManageThread(
                self.get_progression_requirements_for_current_step()
            )
        self.update_flag()

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
                "id": recipe.get("id", ""),
                "image": recipe.get("image", ""),
                "name": recipe.get("name", ""),
                "description": recipe.get("description", ""),
            }
            for recipe in recipes
        ]
        return json.dumps(all_metadata)


# start a instance for the controller
CONTROLLER_INSTANCE = Controller()
