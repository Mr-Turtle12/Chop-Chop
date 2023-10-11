# Controls the flow of the whole of the back-end

import json
import os


class Controller:
    def __init__(self, file_path):
        self.file_path = file_path
        self.recipe_id = None

    def read_recipe(self):
        try:
            with open(self.file_path, 'r') as json_file:
                recipe_data = json.load(json_file)
                recipes = recipe_data.get('recipes', [])
                return recipes  # Return all recipes
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []

    def new_recipe(self, recipe_id):
        self.recipe_id = recipe_id

    def get_command_for_step(self, step_number):
        recipe_data = self.read_recipe()
        if recipe_data:
            steps = recipe_data[0].get('steps', [])
            if 1 <= step_number <= len(steps):
                return steps[step_number - 1].get('command', '')
        return None

    def get_progression_requirements_for_step(self, step_number):
        steps = self.read_recipe()
        if 1 <= step_number < len(steps):
            return [
                steps[step_number - 1].get('progressionObject', ''),
                steps[step_number - 1].get('inhibitor', '')
            ]
        else:
            return None

    def get_recipe_ingredients(self, recipe_id):
        self.new_recipe(recipe_id)
        recipe_data = self.read_recipe()
        ingredients_list = []

        if recipe_data:
            ingredients = recipe_data[0].get('ingredients', [])
            for ingredient in ingredients:
                item = ingredient.get('item', '')
                amount = ingredient.get('amount', '')
                unit = ingredient.get('unit', '')
                ingredients_list.append({
                    'item': item,
                    'amount': amount,
                    'unit': unit
                })

        return ingredients_list


    def get_all_recipe_metadata(self):
        recipe_data = self.read_recipe()
        all_metadata = []

        for recipe in recipe_data:
            metadata = {
                'recipeIMG': recipe.get('recipeIMG', ''),
                'recipeName': recipe.get('recipeName', ''),
                'description': recipe.get('description', '')
            }
            all_metadata.append(metadata)

        return all_metadata

    def get_recipe_metadata(self, recipe_id):
        self.new_recipe(recipe_id)
        step_num = 1
        metadata = {
            'recipeIMG' : '',
            'recipeName': '',
            'description': '',
            'ingredients': [],
            'commands': []
        }

        recipe_data = self.read_recipe()
        if recipe_data:
            metadata['recipeIMG'] = recipe_data[0].get('recipeIMG', '')
            metadata['recipeName'] = recipe_data[0].get('recipeName', '')
            metadata['description'] = recipe_data[0].get('description', '')

            # Use the get_recipe_ingredients function to get ingredients for the specified recipe
            ingredients = self.get_recipe_ingredients(recipe_id)
            metadata['ingredients'] = ingredients

        while True:
            command = self.get_command_for_step(step_num)
            if command is not None:
                metadata['commands'].append(command)
                step_num += 1
            else:
                break

        return metadata


# Example usage
if __name__ == "__main__":
    # Specify the path to the JSON file
    json_file_name = "QSBRecipe.json"
    json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../Database', json_file_name))

    # Initialize Controller
    recipe_reader = Controller(json_file_path)

    # Provide the recipe ID for the recipe you want to retrieve metadata for
    recipe_ID = "1"

    # Test outputs
    recipe_metadata = recipe_reader.get_recipe_metadata(recipe_ID)
    all_recipe_metadata = recipe_reader.get_all_recipe_metadata()

    print(recipe_metadata)
    print(all_recipe_metadata)