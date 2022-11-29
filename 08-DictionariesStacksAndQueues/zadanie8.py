import json

person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

#a      
print(person)
#b
print(person['name'])
#c
print(person['hobby'])
#d
person['surname']='Nowak'
print(person['surname'])
#e
person['married']='False'
print(person['married'])
#f
person['gender']='male'
print(person['gender'])
#g
person['hobby'].append('bycycle')
print(person['hobby'])
#h
person['phone']['work'] = '313131444'
print(person['phone'])