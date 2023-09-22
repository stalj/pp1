a=[2,3,7,5,4]

print(len(a))
print(a[0])
print(a[1:2:])
print(a[-1])
print(a[len(a)-2])
print(a[0]+a[-1])
print(a[2])
for x in a:
    print(x, end=" ")
print()
for x in range(0, int(len(a)/2)+1):
    print(a[x], end=" ")