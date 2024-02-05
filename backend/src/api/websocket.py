import asyncio
import websockets
import json

from backend.src.api.Request import Request
from backend.src.config import WEBSOCKET_UPDATE_INTERVAL, SERVER_IP
from backend.src.controller.controller import CONTROLLER_INSTANCE
from backend.src.utils.utils import log
from backend.src.utils import SQLQueries


# Maintain a list of connected clients
connected_clients = set()


async def consumer_handler(websocket):
    """Handles incoming requests from the client."""
    connected_clients.add(websocket)  # Add client to the set of connected clients
    try:
        while True:
            request = []
            try:
                request = Request(json.loads(await websocket.recv()))
            except json.JSONDecodeError:
                log("!!! Poorly formatted JSON", "API")
                await websocket.send("Poorly formatted JSON")

            match request.matcher:
                # returns basic info for all recipes
                case ("get", 0):
                    log(">>> all recipes' info", "API")
                    await websocket.send(SQLQueries.get_all_metadata())
                # returns basic info for favourite recipes
                case ("get", -1):
                    log(">>> get all favourite recipes' info", "API")
                    await websocket.send(SQLQueries.get_favourites_metadata())

                case ("get", -2):
                    log(">>> get all recipes' info which has AI", "API")
                    await websocket.send(SQLQueries.get_AIs_metadata())

                case ("get", -3):
                    log(">>> get Random recipes", "API")
                    await websocket.send(SQLQueries.get_Random_metadata())

                # returns specific info for one recipe
                case ("get", recipe_id):
                    log(f">>> recipe {recipe_id} info", "API")
                    await websocket.send(
                        CONTROLLER_INSTANCE.get_recipe_metadata(recipe_id)
                    )

                case ("get-search", search_name):
                    log(f">>> search for {search_name}", "API")
                    await websocket.send(SQLQueries.search(search_name))

                # "loads" the recipe to the controller
                case ("start", recipe_id):
                    log(f">>> starting recipe {recipe_id}", "API")
                    CONTROLLER_INSTANCE.new_recipe(recipe_id)
                    await websocket.send(json.dumps({"start": recipe_id}))

                # Sets current step (to be implemented later)
                case ("set", step_number):
                    log(f">>> step set {step_number}", "API")
                    CONTROLLER_INSTANCE.set_step(step_number)
                    await websocket.send(json.dumps({"set": step_number}))

                case ("timer-end", timer_id):
                    log(f">>> timer {timer_id} ended", "API")
                    # in the future we should handle this \/ differently.... but this will do for now
                    CONTROLLER_INSTANCE.progress_next_step()
                    await websocket.send(json.dumps({"end_time": True}))

                case ("favourite", (recipe_id, type)):
                    log(f">>> changing favourite setting for {recipe_id}", "API")
                    SQLQueries.set_favourite(recipe_id, type)
                    await websocket.send(json.dumps({"setting": recipe_id}))

                case ("new_recipe", recipe_metadata):
                    log(f">>> adding a new recipe for {recipe_metadata}", "API")
                    await websocket.send(
                        SQLQueries.insert_recipe_into_database(recipe_metadata)
                    )
                case "end":
                    log(f">>> end the recipe", "API")
                    CONTROLLER_INSTANCE.update_end_flag()
                    await websocket.send(json.dumps({"end": True}))

                case _:
                    log(request.matcher, "API")
                    log("!!! unknown command", "API")
                    await websocket.send("Unknown command")
            await asyncio.sleep(WEBSOCKET_UPDATE_INTERVAL)
    finally:
        connected_clients.remove(
            websocket
        )  # Remove client from the set when connection closes


async def producer_handler():
    """Handles outgoing responses to the client."""
    while True:
        if CONTROLLER_INSTANCE.step_changed_flag.state:
            CONTROLLER_INSTANCE.update_flag()
            new_step = CONTROLLER_INSTANCE.current_recipe.current_step
            new_inhibitors = (
                CONTROLLER_INSTANCE.get_progression_requirements_for_current_step()
            )
            response = {
                "step": new_step,
                "inhibitors": {
                    "camera": new_inhibitors[0],
                    "progressionObject": new_inhibitors[1],
                    "inhibitor": new_inhibitors[2],
                },
            }
            log(f">>> updated step {new_step}", "API")
            await asyncio.gather(
                *[client.send(json.dumps(response)) for client in connected_clients]
            )
        await asyncio.sleep(WEBSOCKET_UPDATE_INTERVAL)


async def handler(websocket, path):
    """Combine both incoming and outgoing handlers."""
    consumer_task = asyncio.create_task(consumer_handler(websocket))
    producer_task = asyncio.create_task(producer_handler())
    await asyncio.gather(consumer_task, producer_task)


def start_websocket():
    """Starts the WebSocket server."""
    start_server = websockets.serve(handler, SERVER_IP, 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
