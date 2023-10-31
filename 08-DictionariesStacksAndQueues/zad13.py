import json
student={
    "name":"Jan",
    "surname":"Doniec",
    "age": 18,
    "university":"Cracow Univeristy of Economics",
    "field of studies":"Applied Informatics",
    "height":179

}

with open("student.json", "w") as f:
    json.dump(student, f)