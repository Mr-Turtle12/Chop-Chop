import sqlite3
from backend.src import config


def SQLiteQuery(Query, one):
    # Connect to the SQLite database
    conn = sqlite3.connect(config.DATABASE)
    cursor = conn.cursor()
    # Fetch recipe data from the database
    cursor.execute(Query)
    if one:
        target_recipe = cursor.fetchone()
    else:
        target_recipe = cursor.fetchall()

    conn.close()
    return target_recipe if target_recipe else None


def get_command(recipe_id):
    SQLCommand = "SELECT command FROM steps WHERE recipe_id=" + str(recipe_id)
    return SQLiteQuery(SQLCommand, False)


def get_all_metadata_from(recipe_id):
    SQLCommand = "SELECT * FROM recipes WHERE id= " + str(recipe_id)

    return SQLiteQuery(SQLCommand, True)


def get_all_metadata():
    return SQLiteQuery("SELECT id , image , name , description FROM recipes", False)


def get_ingredients(recipe_id):
    SQLCommand = "SELECT * FROM ingredients WHERE recipe_id=" + str(recipe_id)
    return SQLiteQuery(SQLCommand, False)
