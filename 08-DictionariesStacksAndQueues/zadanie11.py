import json
movie = {
    "title":"Shutter Island",
    "year": 2010 ,
    "actor":{"leading":"Leonardo DiCaprio","supporting":"Mark Ruffalo"},
    "oscar": False,
    "director": "Martin Scorsese",
    "music":"Philip Stockton"
}
with open("json.json", "w") as file:
    json.dump(movie, file, indent = 6)
