import csv
import re
with open("test.csv") as f:
    a=csv.reader(f,delimiter=',')
    j=[]
    for i in a:
        j.append(re.findall(r"\b\w+\b", i[6]))
    licznik=0
for i in j:
    if (i[-1])=="com":
        licznik=licznik+1
print(licznik)