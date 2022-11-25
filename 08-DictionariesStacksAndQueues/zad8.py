person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person.get("name"))
print(person.get("hobby"))
person.update({"surename": "Nowak"})
person.update({"married": False})
person["gender"]="Male"
person["hobby"].append("bicycle")
person["phone"].update({"phone":"workplace: 313131444"})
print(person)
