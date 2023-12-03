import json

with open("data.json") as file:
    data = json.load(file)
for i in data:
    if i["country"] == "Poland":
        for key, value in i.items():
            print(f"{key}: {value}")
