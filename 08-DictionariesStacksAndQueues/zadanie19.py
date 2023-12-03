import json

with open("students.json", "r") as file:
    data = json.load(file)
limited_data = []
for student in data:
    limited_student = {
        'first name': student['name'],
        'last name': student['surname'],
        'student id': student['student_ID']
    }
    limited_data.append(limited_student)
with open("limited.json", "w") as file1:
    json.dump(limited_data, file1, indent = 2)