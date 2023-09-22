import json

with open("data.json") as file:
    data = json.load(file)

for dict in data:
    for key,value in dict.items():
        print(key,":",value)

