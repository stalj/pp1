import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
sum=0

for x in range(len(temperatures)):
    sum=sum+int(temperatures[x])

print(sum/len(temperatures))