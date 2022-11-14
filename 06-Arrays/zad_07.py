a=[1,2,3,4,5]

print(1-a[0])
print(a[-1]+4)
if len(a)%2==0:
    print(a[len(a)/2]*2)
else:
    print(a[int(len(a)/2) ]*2)
for x in a:
    print(x+3, end=" ")
print()
