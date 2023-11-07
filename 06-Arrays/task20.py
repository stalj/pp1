array = [12, 6, 4, 9, 10]
length = len(array)
for i in range(length):
    print(array[i], int(array[i])*"*")

def star(n):
    for i in range(n):
        s1 = str(n) + " " + n*"*"
    return s1

print(star(7))