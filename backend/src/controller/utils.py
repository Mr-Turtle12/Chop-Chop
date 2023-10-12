import json
import os


def get_database_address(json_file_name):
    return os.getenv("chop-chop-database") + "/" + json_file_name + ".json"


def get_JSON(file):
    # Opening JSON file
    f = open(file)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    return data


# get_JSON(sys.path.)

def fetch_recipe_by_id(recipe_id, recipe_data):
    for recipe in recipe_data.get('recipes', []):
        if recipe.get('id') == recipe_id:
            return recipe
    return None
