import re
numbers=[]
with open("grades.txt", "r") as f:
    for i in f:
        a=i.strip("\n")


numbers = re.findall(r'[0-9][0-9.]+', a)
h=[]
for i in numbers:
    h.append(float(i))
print(h)

mean=sum(h)/len(h)
print(mean)