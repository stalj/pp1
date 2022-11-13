def prównanie(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return 0

def funkcja(x,y):
    if x>y:
        return print(x)
    elif y>x:
        return print(y)
    else:
        return print(0)



print(prównanie(5,4)*prównanie(5,4))

print(funkcja(5,4)*funkcja(5,4))