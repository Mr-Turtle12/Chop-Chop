import keyword
from click import command

"""
request class for chop chop
"""


class Request:
    def __init__(self, jsonRequest: dict):
        command: dict = jsonRequest["command"]
        self.recipe_id: int = command.get("recipe_id", None)
        self.keyword: str = command["keyword"]
        self.step: int = command.get("step", None)

        self.matcher = self.__matcher()

    def __matcher(self):
        match self.keyword:
            case "get" | "start":
                return (self.keyword, self.recipe_id)
            case "step":
                return (self.keyword, self.step)
            case _:
                return None
