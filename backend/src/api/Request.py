from click import command

"""
request class for chop chop
"""


class Request:
    def __init__(self, jsonRequest: dict):
        command: dict = jsonRequest["command"]
        self.recipe_id: int = command["recipe_id"]
        self.keyword: str = command["keyword"]
        self.step: int = command.get("step", None)
