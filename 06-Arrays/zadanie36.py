my_tuple = (50,20,40,50,30,50)
counting_numbers = {}
for i in my_tuple:
    if i in counting_numbers:
        counting_numbers[i] += 1
    else:
        counting_numbers[i] = 1
print('Tuple:', ', '.join(map(str, my_tuple)))
n = int(input('Number: '))
print(f'Number of occurrences: {counting_numbers[n]}')