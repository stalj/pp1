import json

with open("filename.json") as file:
    data = json.load(file)

#for k,v in data.items():
   # print(k,":",v)

i=0
while i<len(data):
    for k,v in data[i].items():
        print(k, ':',v)
    print()
    i+=1