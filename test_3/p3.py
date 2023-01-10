def f(n):
    import re
    x=re.findall(r"[A-ZZ]+[1-9999]\b",n)
    if len(x)!=0:
        return True
    else:
        return False
    
f("G80915")