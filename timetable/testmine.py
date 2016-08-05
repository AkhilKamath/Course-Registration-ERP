import json

with open("data.json") as json_file:
    json_data = json.load(json_file)
    print(json.dumps(json_data[0], indent=4, sort_keys=True))