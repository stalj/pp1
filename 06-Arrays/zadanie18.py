array = [15, 8, 31, 47, 2, 19]
print(*array)
sum=0
for i in array:
    sum += i
print(f'srednia: {(sum/len(array))}', end = ' ')
