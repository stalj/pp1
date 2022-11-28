import json

book={
    "title":"it ends with us",
    "pages":"482",
    "author":"Collen Hoover",
    "type":"prose",
    "gener":"romantic novel"
}

out_file=open('film.json','w')

json.dump(book, out_file, indent=4)

out_file.close()
