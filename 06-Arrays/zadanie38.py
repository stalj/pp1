arr= [15, 38, 7, 23, 14]
print(f'Array: {', '.join(map(str, arr))}')
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
n = float(input('Enternumber form array: '))
x = arr.index(n)
sum = 0
for i in range(x+1, len(arr)):
    sum+=1
print(f'Number of elements that are greater: {sum}')