from backend.src.controller import utils


class Recipe:
    """Class to manage any information about the recipe once it has been chosen."""

    def __init__(self, recipe_id):
        self.current_recipe = utils.fetch_recipe_by_id(
            recipe_id, utils.get_json(utils.get_database_address("Recipes"))
        )
        self.current_step = 1

    def get_recipe_step(self, step_number):
        """Gets the step for the provided step number.
        Args:
            step_number (int): The number of the step to retrieve.
        Returns:
            dict or None: The step if found, otherwise None.
        """
        if self.current_recipe:
            steps = self.current_recipe.get("steps", [])
            if 1 <= step_number <= len(steps):
                return steps[step_number - 1]
        return None

    def increment_step(self):
        """Increments the current step by one."""
        self.current_step += 1

    def set_current_step(self, step_number):
        self.current_step = step_number

    def get_current_step(self):
        """Gets the current step number.
        Returns:
            int: The current step number.
        """
        return self.current_step

    def get_command_for_step(self, step_number):
        """Gets the command for the provided step number.
        Args:
            step_number (int): The number of the step for which the command is needed.
        Returns:
            dict or None: The command for the step if found, otherwise None.
        """
        step = self.get_recipe_step(step_number)
        return {"command": step.get("command", "")} if step else None

    def get_command_for_current_step(self):
        """Gets the command for the current step.
        Returns:
            dict or None: The command for the current step if found, otherwise None.
        """
        return self.get_command_for_step(self.current_step)

    def get_progression_requirements_for_step(self, step_number):
        """Gets the progression requirements for the provided step number.
        Args:
            step_number (int): The number of the step for which the requirements are needed.
        Returns:
            list or None: The progression requirements for the step if found, otherwise None.
        """
        step = self.get_recipe_step(step_number)
        if step:
            return [
                step.get("camera", ""),
                step.get("progressionObject", ""),
                step.get("inhibitor", ""),
            ]
        return None

    def get_progression_requirements_for_current_step(self):
        """Gets the progression requirements for the current step.
        Returns:
            list or None: The progression requirements for the current step if found, otherwise None.
        """
        return self.get_progression_requirements_for_step(self.current_step)

    def get_recipe_metadata(self):
        """Gets the metadata for the current recipe.
        Returns:
            dict or None: The metadata for the current recipe if found, otherwise None.
        """
        if not self.current_recipe:
            return None

        metadata = {
            "image": self.current_recipe.get("image", ""),
            "name": self.current_recipe.get("name", ""),
            "description": self.current_recipe.get("description", ""),
            "ingredients": self.current_recipe.get("ingredients", []),
            "commands": [],
        }

        for step_num in range(1, len(metadata["steps"])):
            command = self.get_command_for_step(step_num)
            metadata["commands"].append(command)

        return metadata
