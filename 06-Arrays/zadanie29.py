arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
s =''
for i in arr1:
    if i not in arr2:
        s += str(i)+' '
print(s)