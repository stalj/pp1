number = float(input("Enter number: "))

if -10 <= number <= 10:
    in_range = True
else:
    in_range = False

print(f"Number in the range <-10,10>: {in_range}")