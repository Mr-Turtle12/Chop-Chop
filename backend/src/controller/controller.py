from backend.src.controller import recipe, utils, manageThread


class Controller:
    """Controls the flow of the whole backend system."""

    def __init__(self):
        self.current_recipe = None
        self.thread_instance = None

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
        """Gets the command for the specified step number this is for frontend.
        Args:
            step_number (int): The step number for which the command is needed.
        Returns:
            str: The command for the specified step.
        """
        return self.current_recipe.get_command_for_step(step_number)

    def get_command_for_current_step(self):
        """Gets the command for the current step this is frontend.
        Returns:
            str: The command for the current step.
        """
        return self.current_recipe.get_command_for_current_step()

    def get_progression_requirements_for_step(self, step_number):
        """Gets the progression requirements for the specified step number this is for backend.
        Args:
            step_number (int): The step number for which the progression requirements are needed.

        Returns:
            dict: The progression requirements for the specified step.
        """
        return self.current_recipe.get_progression_requirements_for_step(step_number)

    def get_progression_requirements_for_current_step(self):
        """Gets the progression requirements for the current step this is for backend.
        Returns:
            dict: The progression requirements for the current step.
        """
        return self.current_recipe.get_progression_requirements_for_current_step()

    def get_recipe_metadata(self):
        """Gets the metadata of the current recipe this is for frontend.
        Returns:
            dict: The metadata of the current recipe.
        """
        return self.current_recipe.get_recipe_metadata()

    def progress_next_step(self):
        """Progresses to the next step in the recipe."""
        self.current_recipe.increment_step()
        self.thread_instance = manageThread.ManageThread(
            self.get_progression_requirements_for_current_step()
        )
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
        return all_metadata


# start a instance for the controller
CONTROLLER_INSTANCE = Controller()
