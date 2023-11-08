import json
import os
import threading
from collections import deque
from backend.src.config import DETECT_THRESHOLD, DETECT_FRAMES


def does_recipe_id_exist(recipe_id):
    """Checks if the provided recipe ID exists.
    Args:
        recipe_id (int): The ID of the recipe.
    """
    print("check if id exist")


def get_database_address(json_file_name):
    """Returns the database address for the specified JSON file.
    Args:
        json_file_name (str): The name of the JSON file.
    Returns:
        str: The complete address of the JSON file.
    """
    return os.getenv("chop-chop-database") + "/" + json_file_name + ".json"


def get_json(file):
    """Loads and returns JSON data from the specified file.
    Args:
        file (str): The path to the JSON file.
    Returns:
        dict: The JSON data from the file.
    """
    try:
        with open(file, "r") as json_file:
            recipe_data = json.load(json_file)
            return recipe_data
    except FileNotFoundError:
        print(f"File not found: {file}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}


def fetch_recipe_by_id(recipe_id, recipe_data):
    """Fetches a recipe by its ID from the provided recipe data.
    Args:
        recipe_id (int): The ID of the recipe to fetch.
        recipe_data (dict): The data containing the recipes.
    Returns:
        dict or None: The recipe if found, otherwise None.
    """
    for recipe in recipe_data.get("recipes", []):
        if int(recipe.get("id")) == recipe_id:
            return recipe
    return None


class LimitedQueue:
    """A limited-size queue with threshold-based averaging functionality."""

    def __init__(self):
        """Initializes the LimitedQueue."""
        self.queue = deque(maxlen=DETECT_FRAMES)

    def append(self, item):
        """Appends an item to the queue.
        Args:
            item (any): The item to be appended.
        """
        self.queue.append(item)

    def get_average(self):
        """Calculates the average based on the elements in the queue.
        Returns:
            bool: True if the average exceeds the threshold, otherwise False.
        """
        if len(self.queue) < DETECT_FRAMES:
            return False
        else:
            true_count = sum(1 for item in self.queue if item is True)
            return true_count >= DETECT_THRESHOLD


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
