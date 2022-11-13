def f(detector):
    plus=0
    minus=0
    for x in detector:
        if x=="+":
            plus+=1
        else:
            minus+=1
    if plus==minus:
        return("True")
    else:
        return("False")

