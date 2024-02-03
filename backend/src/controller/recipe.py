from backend.src.utils import utils, SQLQueries


class Recipe:
    """Class to manage any information about the recipe once it has been chosen."""

    def __init__(self, recipe_id):
        self.recipe_id = recipe_id
        self.current_step = 0

    def get_recipe_step(self, step_number):
        """Gets the step for the provided step number.
        Args:
            step_number (int): The number of the step to retrieve.
        Returns:
            dict or None: The step if found, otherwise None.
        """
        return utils.SQLiteQuery(
            (
                "SELECT progressionObject , inhibtor, camera FROM steps WHERE recipe_id = "
                + (self.current_step + 1)
                + "& step = "
                + (step_number + 1),
            ),
            "one",
        )

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
        step = SQLQueries.SQLiteQuery(
            (
                "SELECT command FROM steps WHERE recipe_id = "
                + (self.current_step + 1)
                + " AND step = "
                + (step_number + 1),
            ),
            "one",
        )
        return {"command": step} if step else None

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
        return SQLQueries.SQLiteQuery(
            "SELECT camera, progressionObject , inhibitor  FROM steps WHERE recipe_id = "
            + str(self.recipe_id)
            + " AND step ="
            + str(step_number+1),
            "one",
        )

    def get_progression_requirements_for_current_step(self):
        """Gets the progression requirements for the current step.
        Returns:
            list or None: The progression requirements for the current step if found, otherwise None.
        """
        return self.get_progression_requirements_for_step(self.current_step)
