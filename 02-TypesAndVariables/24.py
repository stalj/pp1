var = input("Enter vehicle registration number: ")
if var[0:2] == "KR" or var[0:2] == "KK":
    other_var = True
else:
    other_var = False
print(f"Car from Kraków: {other_var}")