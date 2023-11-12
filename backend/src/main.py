# This file is the entry point for the back end
from backend.src.controller import CONTROLLER_INSTANCE
from backend.src.api.websocket import start_websocket
import os
from backend.src.controller.utils import log


def main():
    # Call start up in controller.
    os.environ["chop-chop-database"] = os.path.normpath(
        os.path.join(os.path.dirname(__file__), "../..", "database")
    )
    start_websocket()


if __name__ == "__main__":
    log("Script started...", "API")
    log("Script started...", "Detect")

    main()
