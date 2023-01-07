def f(n):
    n=int(n)
    stronk=""
    if n>0:
        stronk=stronk+n*"/"
        stronk='-'.join([stronk[i:i+5]for i in range(0,len(stronk),5)])
    elif n<=0:
        stronk=stronk+'" "'
    print(stronk)
f(10)
f(0)
f(3)