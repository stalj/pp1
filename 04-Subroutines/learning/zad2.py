def f(binary_number):
    count=0
    t='01'
    for i in binary_number:
        if i not in t:
            count=1
            break
        else:
            pass
    if count!=0:
        return (False)
    else:
        return (True)
print(f("101101"))
print(f("11110100"))