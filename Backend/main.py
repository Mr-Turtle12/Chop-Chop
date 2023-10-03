# This file is the entry point for the back end
from controller import controller
import os


def main():
    # Call start up in controller.
    controller.test_print()
    os.environ["chop-chop-database"] = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "..", "database")
    )
    controller.get_recipe_from_JSON("DemoRecipe")


main()
