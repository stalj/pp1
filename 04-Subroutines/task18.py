def f(digits):
    length = len(digits)
    sum = 0
    for i in range(0, length):
        sum = sum + int(digits[i])

    print(sum)

f("7182")