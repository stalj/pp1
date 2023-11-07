import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
sum = 0
for i in temperatures:
    sum = sum + int(i)
average = sum / int(len(temperatures))
print(average)