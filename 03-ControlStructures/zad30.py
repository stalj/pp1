n=int(input("Wpisz liczbe: "))

primelist=[]

for n in range(2,n):
    prime = True
    for i in range(2,n):
        if (n%i==0):
            prime = False
    if prime:
        primelist.append(n)
print(primelist)