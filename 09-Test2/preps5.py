def f2(a1,a2):
    licznik1=0
    licznik2=0
    for i in a1:
        if len(str(i))==2:
            licznik1=licznik1+1
    for i in a2:
        if len(str(i))==2:
            licznik2=licznik2+1
    if licznik1==licznik2:
        return True
    else:
        return False

