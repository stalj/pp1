import random as r

arr = [r.randint(1, 999), r.randint(1, 999), r.randint(1, 999), r.randint(1, 999), r.randint(1, 999), r.randint(1, 999),
       r.randint(1, 999), r.randint(1, 999)]

var = "|"

for num in arr:
    if num < 10:
        var += f"   {num}|"
    elif num >= 10 and num < 100:
        var += f"  {num}|"
    elif num >= 100:
        var += f" {num}|"

print("-----------------------------------------")
print(var)
print("-----------------------------------------")


# print(arr)