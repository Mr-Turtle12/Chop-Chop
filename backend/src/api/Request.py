import keyword
from click import command


class Request:
    def __init__(self, json_request: dict):
        command: dict = json_request["command"]
        self.recipe_id: int = command.get("recipe_id", None)
        self.keyword: str = command["keyword"]
        self.step_number: int = command.get("step_number", None)
        self.favourite: bool = command.get("type", None)
        self.timer_id: int = command.get("timer_id", None)
        self.matcher = self.__matcher()

    def __matcher(self):
        """returns matcher object as a tuple of (keyword, recipe_id | step_number)"""
        match self.keyword:
            case "get" | "start":
                return (self.keyword, self.recipe_id)
            case "set":
                return (self.keyword, self.step_number)
            case "favourite":
                return (self.keyword, (self.recipe_id, self.favourite))
            case "timer-end":
                return (self.keyword, self.timer_id)
            case _:
                return None


"""
valid request examples:
{
    "command": {
        "keyword": "get",
        "recipe_id": 0
    }
}
{
    "command": {
        "keyword": "start",
        "recipe_id": 1
    }
}
{
    "command": {
        "keyword": "set",
        "step_number": 1
    }
}
"""
