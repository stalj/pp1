def f(pause):
    length = len(pause)
    for i in range(0, length):
        if pause[i] == " ":
            pass
        else:
            print(pause[i], end = "")
    print()

f("1 2 3 4 5")
f("aa bb cc dd")