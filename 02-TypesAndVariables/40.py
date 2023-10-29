number = input("Enter credit card number: ")
# number = "5020312109004442"

n1 = number[:4]
n2 = number[4:8]
n3 = number[8:12]
n4 = number[12:]

number = n1 + " " + n2 + " " + n3 + " " + n4
print(f"Phone number: {number}")