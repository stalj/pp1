def f(x):
    for y in range(len(x)-1):
        print(str(y),end=", ")
    print(x[-1])

a=[3,5,7,9]

print(f(a))