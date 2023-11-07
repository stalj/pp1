def f1(a):
    licznik=0
    for i in a:
        if i%2==0 and i>8:
            licznik=licznik+1
    return licznik

print(f1([13,7,4,16,3,12,8]))