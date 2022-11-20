a=[4,36,12,28,9,44,5] 
b=[5,1,36]

i=0
j=0

c=[]

while i<len(a) and j<len(b):
    if a[i]==b[j]:
        i+=1
    elif a[i]!=b[j]:
        j+=1
        c.append(a[i])

print(c)