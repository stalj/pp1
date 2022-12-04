array = [15, 8, 31, 47, 2, 19]
sum = 0
lenght = len(array)
for i in array:
    print(i, end = " ")

print()
for i in array:
    sum = sum +i

sre = sum/lenght
print(f"arithmetic mean = {sre}")