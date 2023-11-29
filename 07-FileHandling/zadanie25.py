import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("([1-9]{2})C",message)
sum = 0
for i in temperatures:
    sum+=int(i)
print(f"Average tempersture: {sum/len(temperatures)}")