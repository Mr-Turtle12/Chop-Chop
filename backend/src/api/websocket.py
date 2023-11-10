import asyncio
import websockets
import json

from backend.src.api.Request import Request
from backend.src.config import WEBSOCKET_UPDATE_INTERVAL
from backend.src.controller.controller import CONTROLLER_INSTANCE


async def consumer_handler(websocket):
    """Handles incoming requests from the client.
    Args:
        websocket: The WebSocket connection.
    """
    while True:
        request = []
        try:
            request = Request(json.loads(await websocket.recv()))
        except:
            await websocket.send("Poorly formatted JSON")

        print(f"<<< {request.matcher}")

        match request.matcher:
            # returns basic info for all recipes
            case ("get", 0):
                print(">>> all recipes' info")
                await websocket.send(CONTROLLER_INSTANCE.get_all_recipe_metadata())

            # returns specific info for one recipe
            case ("get", recipe_id):
                print(f">>> recipe {recipe_id} info")
                await websocket.send(CONTROLLER_INSTANCE.get_recipe_metadata(recipe_id))

            # "loads" the recipe to the controller
            case ("start", recipe_id):
                print(f">>> starting recipe {recipe_id}")
                CONTROLLER_INSTANCE.new_recipe(recipe_id)
                await websocket.send("Started")

            # Sets current step (to be implemented later)
            case ("step", step_number):
                print(f">>> step set {step_number}")
                CONTROLLER_INSTANCE.set_step(step_number)
                await websocket.send(f"set step {step_number}")
        await asyncio.sleep(WEBSOCKET_UPDATE_INTERVAL)

async def producer_handler(websocket):
    """Handles outgoing responses to the client.
    Args:
        websocket: The WebSocket connection.
    """
    while True:  # run forever
        if CONTROLLER_INSTANCE.step_changed_flag.state:
            print("!!! step changed")
            new_step = CONTROLLER_INSTANCE.current_recipe.current_step
            response = {"step": new_step}
            print(f">>> updated step {new_step}")
            await websocket.send(json.dumps(response))
            CONTROLLER_INSTANCE.step_changed_flag.state = False
        await asyncio.sleep(WEBSOCKET_UPDATE_INTERVAL)


async def handler(websocket):
    """Combine both outgoing handler and incoming handler so they run at the same time.
    Args:
        websocket: The WebSocket connection.
    """
    consumer_task = asyncio.create_task(consumer_handler(websocket))
    producer_task = asyncio.create_task(producer_handler(websocket))
    await asyncio.gather(consumer_task, producer_task)


def start_websocket():
    """Starts the WebSocket server."""
    start_server = websockets.serve(handler, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
