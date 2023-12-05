import mymath

comp = mymath.generate_number()
var = int(input("Pick a number: "))

print(f"Computer picked: {comp}")

if var == comp:
    print("You won the game!")
else:
    print("Loser!")