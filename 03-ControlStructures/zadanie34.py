a = int(input('Enter the amount in PLN: '))
b_5 = 0
b_2 = 0
b_1 = 0
if a%5 != 0 and a%5 != 5:
    b_5 = a//5
    print(f'5zł - {b_5}')
    a = a - b_5*5
    if a%2 != 0 and a%2 != 2:
        b_2 = a//2
        print(f'2zł - {b_2}')
        a = a - b_2*2
        if a%1 == 0:
            b_1 = a//1
            print(f'1zł - {b_1}')
    elif a%2 == 0:
        b_2 = a//2
        print(f'2zł - {b_2}')
        print(f'1zł - {b_1}')
elif a%5 == 0:
    b_5 = a//5
    print(f'5zł - {b_5}')
    print(f'2zł - {b_2}')
    print(f'1zł - {b_1}')
