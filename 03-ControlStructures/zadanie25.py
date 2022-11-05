a=4
b=15
for i in range(a):
    if i == 0 or i == a - 1:
        for j in range(b):
            print('*', end='')
    else:
        print('*', end='')
        for j in range(1, b - 1):
            print(' ', end='')
        print('*', end='')
    print()
