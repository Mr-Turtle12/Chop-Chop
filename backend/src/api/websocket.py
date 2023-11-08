import asyncio
import websockets
import json

from Request import Request


async def handler(websocket):
    request = []
    try:
        request = Request(json.loads(await websocket.recv()))

    except:
        await websocket.send("Poorly formatted JSON")

    print(f"<<< {request}")

    match (request.keyword, request.recipe_id):
        # returns basic info for all recipes
        case ("get", 0):
            print(">>> all recipes' info")
            await websocket.send("recipe info")

        # returns specific info for one recipe
        case ("get", recipe_id):
            print(f">>> recipe {recipe_id} info")
            await websocket.send(f"recipe {recipe_id} info")

        # "loads" the recipe to the controller
        case ("start", recipe_id):
            print(f">>> starting recipe {recipe_id}")
            await websocket.send("recipe start")

        # Sets current step (to be implemented later)
        case ("step", recipe_id):
            print(">>> step set")
            await websocket.send(f"set step {request.step}")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
