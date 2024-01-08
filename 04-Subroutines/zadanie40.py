def f(number):
    number = str(number)
    sum = 0
    digit_count = {}
    for i in number:
        if i in digit_count:
            digit_count[i] += 1
        else:
            digit_count[i] = 1
    for i, count in digit_count.items():
        if count > 1:
            sum += int(i)*count
    return sum
if __name__ == '__main__':
    print(f(1027))
    print(f(230335))
    print(f(513553007))