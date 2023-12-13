with open("int_numbers.txt","a") as f:
    for number in range (1,51):
        f.write(str(number) + "\n")