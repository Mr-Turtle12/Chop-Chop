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
        self.recipe_metadata: str = command.get("recipe_metadata", None)
        self.search_name: str = command.get("search_name", None)
        self.voice: str = command.get("voice", None)
        self.matcher = self.__matcher()

    def __matcher(self):
        """returns matcher object as a tuple of (keyword, recipe_id | step_number)"""
        match self.keyword:
            case "get":
                return (self.keyword, self.recipe_id)
            case "start":
                return (self.keyword, (self.recipe_id, self.voice))
            case "set":
                return (self.keyword, self.step_number)
            case "favourite":
                return (self.keyword, (self.recipe_id, self.favourite))
            case "timer-end":
                return (self.keyword, self.timer_id)
            case "new_recipe":
                return (self.keyword, self.recipe_metadata)
            case "end":
                return self.keyword
            case "get-search":
                return (self.keyword, self.search_name)
            case "get-audio":
                return self.keyword
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
