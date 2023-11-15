def f(x, y):
    sum = 0
    for i in range(x, y+1):
        if i<0 and i%2 ==0:
            sum += 1
    return sum 