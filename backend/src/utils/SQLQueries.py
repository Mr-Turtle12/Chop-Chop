import json
import sqlite3
from backend.src.utils import utils
from backend.src.config import DATABASE


def SQLiteQuery(Query, type):
    # Connect to the SQLite database
    conn = sqlite3.connect(DATABASE)
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
        "SELECT id , image , name , description , favourite FROM recipes WHERE favourite = 1",
        "all",
    )
    return utils.convert_metadata(query)


def get_command(recipe_id):
    SQLCommand = "SELECT command FROM steps WHERE recipe_id=" + str(recipe_id)
    return SQLiteQuery(SQLCommand, "all")


def get_all_metadata_from(recipe_id):
    SQLCommand = "SELECT * FROM recipes WHERE id= " + str(recipe_id)

    return SQLiteQuery(SQLCommand, "one")


def get_all_metadata():
    return utils.convert_metadata(
        SQLiteQuery(
            "SELECT id , image , name , description , favourite FROM recipes", "all"
        )
    )


def get_AIs_metadata():
    query = SQLiteQuery(
        "SELECT id , image , name , description , favourite FROM recipes WHERE AI = 1",
        "all",
    )
    return utils.convert_metadata(query)


def get_ingredients(recipe_id):
    SQLCommand = "SELECT * FROM ingredients WHERE recipe_id=" + str(recipe_id)
    return SQLiteQuery(SQLCommand, "all")


def insert_recipe_into_database(json_data):
    for recipe in json_data["recipes"]:
        # Insert recipe information
        SQLCommandRecipe = (
            "INSERT INTO recipes (image, name, description, prepTime, cookTime, AI, favourite) "
            f"VALUES ('{recipe['image']}', '{recipe['name']}', '{recipe['description']}', '{recipe['prepTime']}', "
            f"'{recipe['cookTime']}', '{0}', '{0}')"
        )
        SQLiteQuery(SQLCommandRecipe, "commit")

        # Get the last inserted recipe ID
        recipe_id = SQLiteQuery("SELECT id FROM recipes ORDER BY id DESC", "one")[0]

        # Insert ingredients
        for ingredient in recipe["ingredients"]:
            SQLCommandIngredient = f"""
                INSERT INTO ingredients (recipe_id, item, amount, unit)
                VALUES ({recipe_id}, '{ingredient["item"]}', '{ingredient["amount"]}', '{ingredient["unit"]}')
            """
            SQLiteQuery(SQLCommandIngredient, "commit")

        # Insert steps
        for step in recipe["steps"]:
            SQLCommandStep = f"""
                INSERT INTO steps (recipe_id, step, command)
                VALUES ({recipe_id}, '{step["step"]}', '{step["command"]}')
            """
            SQLiteQuery(SQLCommandStep, "commit")


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
