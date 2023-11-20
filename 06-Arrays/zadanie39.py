arr = [15, 38, 7, 23, 14, 18]
for i in range(len(arr)):
    for j in range(0, len(arr)-i-1):
        if arr[j]%2!=0 and arr[j+1]%2 == 0:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)