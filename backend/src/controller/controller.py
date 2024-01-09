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
        SQLCommand = "SELECT * FROM recipes WHERE id= " + str(recipe_id)

        target_recipe = utils.SQLiteQuery(SQLCommand, True)
        if not target_recipe:
            return None
        metadata = {
            "image": target_recipe[1],
            "name": target_recipe[2],
            "description": target_recipe[3],
            "ingredients": utils.get_ingredients(recipe_id),
            "commands": utils.get_commands(recipe_id),
        }
        return metadata

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
        recipes = utils.SQLiteQuery(
            "SELECT id , image , name , description FROM recipes", False
        )
        if not recipes:
            return json.dumps({})
        all_metadata = [
            {
                "id": recipe[0],
                "image": recipe[1],
                "name": recipe[2],
                "description": recipe[3],
            }
            for recipe in recipes
        ]
        return json.dumps(all_metadata)


# start a instance for the controller
CONTROLLER_INSTANCE = Controller()
