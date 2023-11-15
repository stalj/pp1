a = int(input('Enter quanity of prime numbers: '))
i = 1
b = 2
array = []
while i>0:
    if b == 2 or b == 3 or b == 5 or b ==7:
        array.append(b)  
    elif b%2 != 0 and b%3 != 0 and b%7 != 0 and b%5 != 0:
        array.append(b)  
    b = b+1
    i = i+1
    if len(array) == a:
        break
print(*array)
