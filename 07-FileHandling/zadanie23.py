import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
sum=0
for i in temperatures:
    i=int(i)
    sum+=i
a = (sum/len(temperatures))
print(message)
print(f'the average temperature: {a}')