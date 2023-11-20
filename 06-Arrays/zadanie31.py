arr = [2, 3, 2, 5, 8, 1, 9, 8]
counting_numbers = {}
arr2=[]
for i in arr:
    if i in counting_numbers:
        counting_numbers[i] +=1
    else:
        counting_numbers[i] = 1
for i, count in counting_numbers.items():
    if count == 1:
        arr2.append(i)
print('Array:',*arr, sep = ' ')
print('Unique elements:',*arr2, sep = ' ')