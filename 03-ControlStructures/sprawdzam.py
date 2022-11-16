
def f(first_letters):
    length = len(first_letters)
    print(first_letters[0], end= "")
    for i in range(0, length):
        if first_letters[i] == " ":
            print(first_letters[i+1])
        else:
            pass
    print()

f("blue water") 
f("to be or not to be") 
f("Cracow Poland")

