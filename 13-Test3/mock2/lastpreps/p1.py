def f(n):
    n=int(n)
    a=''
    if n>0:
        a=a+"/"*n
        a='-'.join(a[i:i+5] for i in range(0,len(a),5))
        return a
    else:
        return a 

def main():
    # function testing
    print(f(-4))
    print(f(0))
    print(f(5))
    print(f(7))
    print(f(10))
    print(f(11))
if __name__ == "__main__":
    main()
