import base64
import json
import os
import sqlite3
from backend.src.utils import utils
from backend.src.config import DATABASE
from backend.src.utils import SpellChecker


def SQLiteQuery(Query, type):
    # Connect to the SQLite database
    # "../../../database/recipes.db"
    conn = sqlite3.connect(DATABASE + "/recipes.db")
    cursor = conn.cursor()
    # Fetch recipe data from the database
    cursor.execute(Query)
    if type == "one":
        target_recipe = cursor.fetchone()
    elif type == "all":
        target_recipe = cursor.fetchall()
    else:
        conn.commit()
        target_recipe = None

    conn.close()
    return target_recipe if target_recipe else None


def set_favourite(recipe_id, favourite):
    update_query = (
        f"UPDATE recipes SET favourite = "
        + str(int(favourite))
        + " WHERE id = "
        + str(recipe_id)
    )
    return SQLiteQuery(update_query, "commit")


def get_favourites_metadata():
    query = SQLiteQuery(
        "SELECT id , image , name , description , favourite, AI FROM recipes WHERE favourite = 1",
        "all",
    )
    return utils.convert_metadata(query)


def get_command(recipe_id):
    SQLCommand = "SELECT command FROM steps WHERE recipe_id=" + str(recipe_id) + " ORDER BY step"
    return SQLiteQuery(SQLCommand, "all")


def get_all_metadata_from(recipe_id):
    SQLCommand = "SELECT * FROM recipes WHERE id= " + str(recipe_id)

    return SQLiteQuery(SQLCommand, "one")


def get_all_metadata():
    return utils.convert_metadata(
        SQLiteQuery(
            "SELECT id , image , name , description , favourite, AI FROM recipes", "all"
        )
    )


def get_AIs_metadata():
    query = SQLiteQuery(
        "SELECT id , image , name , description , favourite, AI FROM recipes WHERE AI = 1",
        "all",
    )
    return utils.convert_metadata(query)


def get_ingredients(recipe_id):
    SQLCommand = "SELECT * FROM ingredients WHERE recipe_id=" + str(recipe_id)
    return SQLiteQuery(SQLCommand, "all")


def search(query):
    SQLCommand = "SELECT name FROM recipes WHERE name LIKE '%" + query + "%'"
    result = SQLiteQuery(SQLCommand, "all")

    if not result:
        corrected_query = SpellChecker.wordChecker(query)
        if corrected_query:
            query = corrected_query

    SQLCommand = (
        "SELECT * FROM recipes WHERE name LIKE '%" + query + "%' ORDER BY "
        "CASE WHEN name LIKE '" + query + "%' THEN 1 "
        "WHEN name LIKE '% " + query + "%' THEN 2 "
        "WHEN name LIKE '%" + query + "%' THEN 3 ELSE 4 END, name;"
    )
    result = SQLiteQuery(SQLCommand, "all")

    return utils.convert_metadata(result)


def insert_recipe_into_database(json_data):
    # Insert recipe information
    SQLCommandRecipe = (
        f"INSERT INTO recipes (image, name, description, prepTime, cookTime, AI, favourite) "
        f"VALUES ('{json_data['image']}', '{json_data['name']}', '{json_data['description']}', '{json_data['prepTime']}', "
        f"'{json_data['cookTime']}', '{0}', '{0}')"
    )
    SQLiteQuery(SQLCommandRecipe, "commit")

    # Get the last inserted recipe ID
    recipe_id = SQLiteQuery("SELECT id FROM recipes ORDER BY id DESC", "one")[0]

    # Insert ingredients
    for ingredient in json_data["ingredients"]:
        SQLCommandIngredient = f"""
                INSERT INTO ingredients (recipe_id, item, amount, unit)
                VALUES ({recipe_id}, '{ingredient["item"]}', '{ingredient["amount"]}', '{ingredient["unit"]}')
            """
        SQLiteQuery(SQLCommandIngredient, "commit")

    # Insert steps
    for step in json_data["steps"]:
        SQLCommandStep = f"""
                INSERT INTO steps (recipe_id, step, command)
                VALUES ({recipe_id}, '{step["step"]}', '{step["command"]}')
            """
        SQLiteQuery(SQLCommandStep, "commit")

    insert_recipe_into_dictionary(json_data["name"])
    return json.dumps(recipe_id)


def insert_recipe_into_dictionary(recipe_name):
    recipeName = recipe_name.split()
    unimportantWords = ["and", "with", "a", "in", "&", "also"]
    # "../../../database/dictionary.txt"
    dictionary = open(DATABASE + "/dictionary.txt", "a")
    for word in recipeName:
        if word not in unimportantWords and not check_word(word):
            dictionary.write(word + "\n")


def check_word(word):
    with open(DATABASE + "/dictionary.txt", "r") as file:
        for line in file:
            if word.strip() == line.strip():
                return True
    return False


def insert_recipe_into_dictionary(recipe_name):
    recipeName = recipe_name.split()
    unimportantWords = ["and", "with", "a", "in", "&", "also"]
    # "../../../database/dictionary.txt"
    dictionary = open(DATABASE + "/dictionary.txt", "a")
    for word in recipeName:
        if word not in unimportantWords and not check_word(word):
            dictionary.write(word + "\n")


def check_word(word):
    with open(DATABASE + "/dictionary.txt", "r") as file:
        for line in file:
            if word.strip() == line.strip():
                return True
    return False


def get_Random_metadata():
    target_recipe = SQLiteQuery(
        "SELECT id , image , name , description  FROM recipes ORDER BY RANDOM()",
        "one",
    )
    if not target_recipe:
        return None
    metadata = {
        "id": target_recipe[0],
        "image": utils.convert_image(target_recipe[1]),
        "name": target_recipe[2],
        "description": target_recipe[3],
    }
    return json.dumps(metadata)


def is_smart(recipe_id):
    query = SQLiteQuery("SELECT AI FROM recipes WHERE id = " + str(recipe_id), "one")
    return query[0]
