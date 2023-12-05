import json

with open("filename.json") as file:
    data = json.load(file)

# z jsona robi się słownik, albo tablica, albo i jedno i drugie

for key,value in data.items():
    print(f"{key} : {value}")
