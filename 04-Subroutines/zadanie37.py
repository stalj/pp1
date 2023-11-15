def f(n):
    array = []
    if n == 1:
        array.append(0)
    if n >= 2:
        array = [0,1]
    for i in range (n):
        array.append(array[i]+array[i+1])
    return array[n-1]

if __name__ == '__main__':
    print(f(5))
    print(f(9))