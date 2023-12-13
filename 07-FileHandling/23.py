with open("pow_numbers.txt","w") as f:
    for number in range(1,11):
        f.write(f"{number ** 1}, {number ** 2}, {number ** 3}\n")