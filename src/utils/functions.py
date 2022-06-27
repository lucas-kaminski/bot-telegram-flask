import json

def setAvaliableCommandsJson():
    with open("src/json/commands.json", encoding="utf8") as json_file:
        commands = json.load(json_file)["commands"]

    available_commands = {"available_commands": []}
    for command in commands:
        available_commands["available_commands"].append(command["command"])

    with open("src/json/availableCommands.json", "w", encoding="utf8") as json_file:
        json.dump(available_commands, json_file)
