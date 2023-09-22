a=[12, 6, 4, 9, 10]

def star(n):
    for x in range(len(n)):
        print(a[x],":",end=" ")
        for y in range(a[x]):
            print("*",end=" ")
        print()

star(a)