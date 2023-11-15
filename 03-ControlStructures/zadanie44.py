i = 1
array = []
while i > 0:
    a = int(input('Enter number (enter 0 if you want to stop): '))
    array.append(a)
    if a == 0:
        break
    i = i + 1
print(f'RESULT: Quantity = {i-1}, Sum = {sum(array)}, Mean = {sum(array)/(i-1)}')