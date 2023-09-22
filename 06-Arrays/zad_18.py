a=[15, 8, 31, 47, 2, 19]

art=0

for x in range(len(a)):
    print(a[x],end=" ")
    art+=a[x]

print()
print(art/len(a))