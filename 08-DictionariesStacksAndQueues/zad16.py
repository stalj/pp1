import json
with open("students.json", "r") as f:
    students=json.load(f)

with open("limited.json", "w") as j:
    for i in students:
        j.write(i["first_name"])
        j.write(" ")
        j.write(i["last_name"])
        j.write(" ")
        j.write(str(i["id"]))
        j.write("\n") 
        #print(i['first_name'],i['last_name'],i['id'])
    
    
    