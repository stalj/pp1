var = "Mr. John May, born on 1998-02-16"

print(f"Description: {var}")
print(f"Name: {var[4:8]}")
print(f"Surname: {var[9:12]}")
print(f"Initials: {var[4] + var[9]}")
print(f"Born: {var[-11:]}")