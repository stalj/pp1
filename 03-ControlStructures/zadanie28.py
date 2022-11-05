fib0=0
fib1 = fib2 = 1
n = 49
print(fib0,fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2 #f1 присваивается f2, а f2 присваивается fib1 + fib2
    print(fib2, end=' ') 