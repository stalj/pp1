person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person.values())
print(person["name"])
print(person["hobby"])
person["surname"]="Nowak"
print(person["surname"])
person["married"]=False
print(person["married"])
person["gender"]="male"
person["hobby"]+=["bicycle"]
person["phone"]["workphone"]="31313444"
print(person)
