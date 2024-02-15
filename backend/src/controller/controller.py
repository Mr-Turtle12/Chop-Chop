import base64
import json
from backend.src.controller import recipe, manageThread
from backend.src.config import SERVER_IP
from backend.src.interpreter import create_camera, destroy_camera
from backend.src.utils import utils, SQLQueries


class Controller:
    """Controls the flow of the whole backend system."""

    def __init__(self):
        self.current_recipe = None
        self.thread_instance = None
        self.step_changed_flag = utils.StepChangeFlag()
        self.end_flag = utils.EndFlag()
        self.AIvoice = "Wallace"
        self.Cameras = None

    def new_recipe(self, recipe_id):
        """Starts a new recipe with the given recipe ID.
        Args:
            recipe_id (int): The ID of the recipe to start.
        """
        self.current_recipe = recipe.Recipe(recipe_id)
        self.end_flag.clear()
        self.Cameras = create_camera()
        if SQLQueries.is_smart(self.current_recipe.recipe_id):
            self.thread_instance = manageThread.ManageThread(
                self.get_progression_requirements_for_current_step(),
                self.end_flag,
                self.Cameras,
            )

    def update_flag(self):
        self.step_changed_flag.state = not self.step_changed_flag.state

    def update_end_flag(self):
        self.end_flag.set()

    def get_command_for_step(self, step_number):
        return self.current_recipe.get_command_for_step(step_number)

    def get_command_for_current_step(self):
        return self.current_recipe.get_command_for_current_step()

    def get_progression_requirements_for_step(self, step_number):
        return self.current_recipe.get_progression_requirements_for_step(step_number)

    def get_progression_requirements_for_current_step(self):
        return self.current_recipe.get_progression_requirements_for_current_step()

    def get_recipe_metadata(self, recipe_id):
        target_recipe = SQLQueries.get_all_metadata_from(recipe_id)
        if not target_recipe:
            return None

        print(target_recipe)
        metadata = {
            "image": utils.convert_image(target_recipe[1]),
            "name": target_recipe[2],
            "description": target_recipe[3],
            "ingredients": utils.get_ingredients(recipe_id),
            "prepTime": target_recipe[4],
            "cookTime": target_recipe[5],
            "isFavourite": bool(target_recipe[7]),
            "commands": utils.get_commands(recipe_id),
            "isSmart": bool(SQLQueries.is_smart(recipe_id)),
            "servingSize": target_recipe[8],
        }
        return json.dumps(metadata)

    def get_audio_URL(self):
        return f"http://{SERVER_IP}:8000/photos/{self.current_recipe.recipe_name.replace(' ', '_')}/{self.AIvoice}_{self.current_recipe.current_step+1}.mp3"

    def progress_next_step(self):
        """Progresses to the next step in the recipe."""
        self.current_recipe.increment_step()
        if SQLQueries.is_smart(self.current_recipe.recipe_id):
            self.thread_instance = manageThread.ManageThread(
                self.get_progression_requirements_for_current_step(),
                self.end_flag,
                self.Cameras,
            )
        self.update_flag()

    def set_step(self, step_numer):
        if self.current_recipe is not None:
            self.current_recipe.set_current_step(step_numer)
            if SQLQueries.is_smart(self.current_recipe.recipe_id):
                self.thread_instance = manageThread.ManageThread(
                    self.get_progression_requirements_for_current_step(),
                    self.end_flag,
                    self.Cameras,
                )
        self.update_flag()


# start a instance for the controller
CONTROLLER_INSTANCE = Controller()
