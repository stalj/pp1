import random
arr = []
s = '|'
a = 0
for i in range(8):
    arr.append(random.randint(1,999))
for j in arr:
    s += ' '*(4 - len(str(arr[a]))) + str(j)+'|'
    a+=1
print('-'*((len(arr)*5)+1))
print(s)
print('-'*((len(arr)*5)+1))
