import json

students=[{
    'name':'Norbert',
    'height': 176,
    'eye_color':'blue',
    'tatu': None},

    {'name':'Zuzanna',
    'height': 154,
    'eye_color':'blue',
    'tatu': None},

    {'name':'Bartek',
    'height': 184,
    'eye_color':'green',
    'tatu': None }]

with open('students.json', 'w') as file:
    data = json.dump(students, file, indent=3)