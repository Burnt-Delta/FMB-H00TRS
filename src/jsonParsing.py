# jsonParsing.py - provides all json file interaction
# Author: Burnt-Delta

import json

# converts given json file to a dict
def jsonToDict(file):
    with open(("../json/" + file), "r") as file:
        data = json.load(file)
        file.close()
    return data

# returns a tuple containing username and PAT
def getAuth():
    data = jsonToDict("config.json")
    auth = data['auth']

    return auth['Username'], auth['PAT']
