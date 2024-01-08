a = int(input('Enter longer side of a rectangle: '))
b = int(input('Enter shorter side of a rectangle: '))
c = '*'
d = 1

while d < b:
    while (d == 1 or d == b):
        print (a*c)
        d = d+1
        while d > 1 and d < b:
            print (f'{c}{(a-2)*' '}{c}')
            d = d + 1

