def f(n1,n2,n3,n4):
    ujemne=0
    dodatnie=0
    list=[n1,n2,n3,n4]
    for i in list:
        if i>=0:
            dodatnie+=1
        else:
            ujemne+=1

    if ujemne == 2:
        return True
    else:
        return False

f(-2,9,-7,6)
f(-6,-8,-7,7)