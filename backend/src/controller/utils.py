import json
import os


def does_recipe_id_exist(recipe_id):
    # Check if ID is in the JSON files
    print("check if id exist")


def get_database_address(json_file_name):
    return os.getenv("chop-chop-database") + "/" + json_file_name + ".json"


def get_json(file):
    try:
        with open(file, 'r') as json_file:
            recipe_data = json.load(json_file)
            return recipe_data
    except FileNotFoundError:
        print(f"File not found: {file}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}


def fetch_recipe_by_id(recipe_id, recipe_data):
    for recipe in recipe_data.get('recipes', []):
        if int(recipe.get('id')) == recipe_id:
            return recipe
    return None
