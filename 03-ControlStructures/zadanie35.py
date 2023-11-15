array = []
for a in range(1, 31):
    if a%3 == 0 and a%15 != 0:
        b = 'THREE'
    elif a%5 == 0 and a%15 != 0:
        b = 'FIVE'
    elif a%15 == 0:
        b = 'BINGO'
    else:
        b = a
    array.append(b)
print(*array, sep=", ")