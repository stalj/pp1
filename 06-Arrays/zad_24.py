a=[2,3,2,5,8,1,9,8]
b=a.copy()
i=0
c=b[i]
for x in range(len(a)):
    if a[x]==c:
        i+=1
        b.remove(c)
print(b)