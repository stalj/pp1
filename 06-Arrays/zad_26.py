a=[5,1,9,6,1]
b=a[0]

for x in range(len(a)):
    if a[x]>=b:
        b=a[x]
        i=x
a.pop(i)

c=a[0]
for y in range(len(a)):
    if a[y]>=c:
        c=a[y]
print(c)
