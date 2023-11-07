def numbers(n):
    arr = []
    for i in range(n):
        arr.append(str(i+1)) 
    return " ".join(arr)
print(numbers(9))

def number(n):
    num = ''
    for m in range(1, n+1):
        num+=str(m)
        num+= ' '
    return num
print(number(6))