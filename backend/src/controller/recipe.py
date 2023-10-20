from backend.src.controller import utils


class Recipe:
    def __init__(self, recipe_id):
        self.current_recipe = utils.fetch_recipe_by_id(
            recipe_id, utils.get_json("Recipes")
        )
        self.current_step = 1

    def get_recipe_step(self, step_number):
        if self.current_recipe:
            steps = self.current_recipe.get("steps", [])
            if 1 <= step_number <= len(steps):
                return steps[step_number - 1]
        return None

    def get_current_step(self):
        return self.current_step

    def get_command_for_step(self, step_number):
        step = self.get_recipe_step(step_number)
        return {"command": step.get("command", "")} if step else None

    def get_command_for_current_step(self):
        return self.get_command_for_step(self.current_step)

    def get_progression_requirements_for_step(self, step_number):
        step = self.get_recipe_step(step_number)
        if step:
            return [
                step.get("camera", ""),
                (step.get("progressionObject", ""), step.get("inhibitor", "")),
            ]
        return None

    def get_progression_requirements_for_current_step(self):
        return self.get_progression_requirements_for_step(self.current_step)

    def get_recipe_metadata(self):
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

    ## Go forward step
    ## Go back step
    ## use get_progression_requirements_for_step to serve to interpreter and then change current step based on response
