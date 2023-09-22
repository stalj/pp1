def max(array1):
    y=array1[0]
    for x in array1:
        if x==y or x>y:
            y=x
    return y

def min(array2):
    i=array2[0]
    for j in array2:
        if j==i or j<i:
            i=j
    return i

c=[0,4,7,-5]

print(min(c))
print(max(c))