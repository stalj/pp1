def f(password):
    x=str(password)
    if len(password)>=6:
        for i in str(password):
            for j in range(1,len(password)):
                if str(password)[j]!=str(password)[j+1]:
                    return True
                else:
                    return False
    else:
        return False


