question1 = (input("Do you like trains? (Y/N): ")).lower()
question2 = (input("Do you like lolis? (Y/N): ")).lower()
question3 = (input("Do you like trans-continental nuclear submarines carrying over 25 "
                   "mega-tons of weaponary? (Y/N): ")).lower()

result1 = None
result2 = None
result3 = None

if question1 == "y":
    result1 = True
else:
    result1 = False

if question2 == "y":
    result2 = True
else:
    result2 = False

if question3 == "y":
    result3 = True
else:
    result3 = False

print(result1, result2, result3)