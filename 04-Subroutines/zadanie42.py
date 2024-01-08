def f(n1, n2, n3):
    array = [n1,n2,n3]
    return max(array) - min(array)

if __name__ == '__main__':
    print(f(7,4,9))
    print(f(2, 12, 8))