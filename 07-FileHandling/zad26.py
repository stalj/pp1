import re
x=[]
with open("countries.txt","r") as f:
    for i in f:
        x.append(i.strip("\n"))
a=" "
s=" "
s = ','.join([str(elem) for elem in x])
#print(s)
pattern='([^a-z\s])|((^|\s)[a-z]{6,}(\s|$))'

regex = re.compile(pattern)
with open("countries.txt") as f:
    for line in f:
        result = regex.search(line)
print(result)