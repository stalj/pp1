def f(letters):
    length = len(letters)
    sum = 0
    for i in range(0, length):
        if letters[i] == "e":
            sum = sum+1
        else:
            pass
    print(sum)

f("You never get a second chance to make a first impression")