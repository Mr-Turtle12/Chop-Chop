import json
import os


class Controller:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recipe_data = self.read_recipe()
        self.current_recipe = None

    def read_recipe(self):
        try:
            with open(self.file_path, 'r') as json_file:
                recipe_data = json.load(json_file)
                return recipe_data
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}

    def switch_recipe(self, recipe_id):
        for recipe in self.recipe_data.get('recipes', []):
            if recipe.get('id') == recipe_id:
                self.current_recipe = recipe
                return True
        self.current_recipe = None
        return False

    def get_command_for_step(self, step_number):
        if self.current_recipe:
            steps = self.current_recipe.get('steps', [])
            if 1 <= step_number <= len(steps):
                return steps[step_number - 1].get('command', '')
        return None

    def get_progression_requirements_for_step(self, step_number):
        if self.current_recipe:
            steps = self.current_recipe.get('steps', [])
            if 1 <= step_number <= len(steps):
                step = steps[step_number - 1]
                return [
                    step.get('camera', ''),
                    (step.get('progressionObject', ''), step.get('inhibitor', ''))
                ]
        return None

    def get_recipe_metadata(self):
        if not self.current_recipe:
            return None

        metadata = {
            'image': self.current_recipe.get('image', ''),
            'name': self.current_recipe.get('name', ''),
            'description': self.current_recipe.get('description', ''),
            'ingredients': self.current_recipe.get('ingredients', []),
            'commands': [],
        }

        step_num = 1
        while True:
            command = self.get_command_for_step(step_num)
            if command is not None:
                metadata['commands'].append(command)
                step_num += 1
            else:
                break

        return metadata

    def get_all_recipe_metadata(self):
        all_metadata = []

        for recipe in self.recipe_data.get('recipes', []):
            metadata = {
                'image': recipe.get('image', ''),
                'name': recipe.get('name', ''),
                'description': recipe.get('description', ''),
            }
            all_metadata.append(metadata)

        return all_metadata


# Example usage
if __name__ == "__main__":
    # Specify the path to the JSON file
    json_file_name = "QSBRecipe.json"
    json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Database', json_file_name))

    # Initialize Controller
    recipe_reader = Controller(json_file_path)

    # Switch to a specific recipe by ID
    recipe_id = "1"
    if recipe_reader.switch_recipe(recipe_id):
        # Test outputs
        print(recipe_reader.get_progression_requirements_for_step(1))
        print(recipe_reader.get_recipe_metadata())

    # Switch to another recipe
    recipe_id = "2"
    if recipe_reader.switch_recipe(recipe_id):
        # Test outputs
        print(recipe_reader.get_progression_requirements_for_step(1))
        print(recipe_reader.get_recipe_metadata())

    # Get metadata for all recipes
    all_recipe_metadata = recipe_reader.get_all_recipe_metadata()
    print(all_recipe_metadata)