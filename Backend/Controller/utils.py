import json
import os


def get_database_address(json_file_name):
    return os.getenv("chop-chop-database") + "/" + json_file_name + ".json"


def get_JSON(file):
    # Opening JSON file
    f = open(file)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data["Steps"]:
        print(i)

    # Closing file
    f.close()

    return data


# get_JSON(sys.path.)
