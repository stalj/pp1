def f(a):
    array=[]
    for i in range (a):
        array.append('*')
    return print(*array, sep='/')
if __name__ == '__main__':
    f(4)
    f(1)