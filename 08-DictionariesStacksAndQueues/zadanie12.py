import json
film = {
    'nazwa' : 'Pirates of the Caribbean',
    'aktor' : 'Johnny Depp',
    'genre': 'adventures',
    'budget': '1,145 billions',
    'year' : '2003-2017'
}

json_file = open('favorite.json','w')
json.dump(film, json_file, indent=3)

json_file.close()

