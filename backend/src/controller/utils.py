import json
import sqlite3
import os
import threading
from collections import deque
from backend.src import config


def log(message, type):
    log_file_path = None
    match type:
        case "API":
            log_file_path = config.API_LOG_PATH
        case "Detect":
            log_file_path = config.DETECT_LOG_PATH

    with open(log_file_path, "a") as log_file:
        log_file.write(str(message) + "\n")


def does_recipe_id_exist(recipe_id):
    """Checks if the provided recipe ID exists.
    Args:
        recipe_id (int): The ID of the recipe.
    """
    print("check if id exist")


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


def get_ingredients(recipe_id):
    SQLCommand = "SELECT * FROM ingredients WHERE recipe_id=" + str(recipe_id)
    ingredients = SQLiteQuery(SQLCommand, False)
    # Transform ingredients into a list of dictionaries
    ingredient_list = [
        {"item": i[2], "amount": i[3], "unit": i[4]} for i in ingredients
    ]

    return ingredient_list


def get_commands(recipe_id):
    SQLCommand = "SELECT command FROM steps WHERE recipe_id=" + str(recipe_id)
    commands = SQLiteQuery(SQLCommand, False)
    # Flatten the list of commands
    command_list = [command[0] for command in commands]

    return command_list


class LimitedQueue:
    """A limited-size queue with threshold-based averaging functionality."""

    def __init__(self):
        """Initializes the LimitedQueue."""
        self.queue = deque(maxlen=config.DETECT_FRAMES)

    def append(self, item):
        """Appends an item to the queue.
        Args:
            item (any): The item to be appended.
        """
        self.queue.append(item)

    def get_queue(self):
        """Returns the entire queue."""
        return list(self.queue)

    def get_average(self):
        """Calculates the average based on the elements in the queue.
        Returns:
            bool: True if the average exceeds the threshold, otherwise False.
        """
        if len(self.queue) < config.DETECT_FRAMES:
            return False
        else:
            true_count = sum(1 for item in self.queue if item is True)
            return true_count >= config.DETECT_THRESHOLD


class BaseThread(threading.Thread):
    """A base thread class with callback functionality."""

    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop("target")
        super(BaseThread, self).__init__(
            target=self.target_with_callback, *args, **kwargs
        )
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self):
        """Executes the thread's target method and the callback method if available."""
        self.method()
        if self.callback is not None:
            self.callback(*self.callback_args)


class StepChangeFlag:
    def __init__(self):
        self.state = False
