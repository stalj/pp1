def function(binary_number: str):
    correct = True
    for iteration in binary_number:
        if iteration == "0" or iteration == "1":
            continue
        else:
            correct = False

    return correct

var = input("Gimme a binary number: ")
print(function(var))
