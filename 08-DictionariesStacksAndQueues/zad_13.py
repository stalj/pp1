import json

uczen={
    "imie":"Jan",
    "nazwisko":"Nowak",
    "numer indeksu":111111,
    "wiek":19,
    "pelnoletni":True
}

out_file=open('student.json','w')

json.dump(uczen, out_file, indent=4)

out_file.close()