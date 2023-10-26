# This file is the entry point for the back end
from backend.src import controller
import os


def main():
    # Call start up in controller.
    os.environ["chop-chop-database"] = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "../..", "database")
    )


main()
