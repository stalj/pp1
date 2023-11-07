name1 = input("enter name: ")
age1 = int(input("enter age: "))
name2 = input("enter name: ")
age2 = int(input("enter age: "))

if age1 >= 18 and age2 >= 18:
    print(f"Both {name1} and {name2} are adults")
elif age1 >= 18 and age2 < 18:
    print(f"Only {name1} is an adult")
elif age2 >= 18 and age1 < 18:
    print(f"Only {name2} is an adult")
else:
    print(f"Neither {name1} nor {name2} are adults.")