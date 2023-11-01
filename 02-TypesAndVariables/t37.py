def slicing():
    personel_data = "Mr. John May, born on 1998-02-16"
    name = personel_data[4:8]
    surname = personel_data[9:12]
    initials = personel_data[4] + personel_data[9]
    born = personel_data[22:]
    result = f'Name: {name}\nSurname: {surname}\nInitials: {initials}\nBorn: {born}'

    return result
    



print(slicing())