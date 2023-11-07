age = int(input("Enter dog age: "))
sum = 0

for thing in range(1,age +1):
    if thing <= 2:
        sum += 10.5
    else:
        sum += 4

print(f"In Dawg years, it's {int(sum)} years old.")