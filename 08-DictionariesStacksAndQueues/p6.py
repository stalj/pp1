import json

with open("data.json") as file:
    file_open=json.load(file)
i=0
sum=0
while i<10:
    if file_open[i]["age"]<20 and file_open[i]["gender"]=="Male":
        sum+=1
    i+=1
print(sum)