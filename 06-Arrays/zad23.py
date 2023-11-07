x=[5,2,1,3,7]
n=len(x)
swapped=False
for i in range(n-1):
    for j in range(0, n-i-1):
        if x[j]>x[j+1]:
            swapped=True
            x[j], x[j+1]=x[j+1], x[j]
    if not swapped:
        continue

print(x)