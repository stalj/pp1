a=int(input("Podaj długość jednego z boków prostokąta:"))
b=int(input("Podaj długość drugiego boku prostokąta:"))

print("* "*a, end="  ")
print()

for x in range(b):
    print("* ", end=" "*(a*2-4),)
    print("*")
    print()


print("* "*a, end="  ")
print()
