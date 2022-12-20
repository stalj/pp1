import json
book={
    "main_char_name":"Jack Reacher",
    "gener":"male",
    "occupation":"U.S. Military Police Corps",
    "rank":"Major",
    "born":"1960",
    "height":"195cm"
}

with open("favourite.json", "w") as f:
    json.dump(book, f)