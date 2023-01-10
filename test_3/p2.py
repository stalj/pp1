def f(c,n):
    wiecej=0
    mniej=0
    for x in c:
        if x>=n:
            wiecej+=1
        else:
            mniej+=1
    return wiecej, mniej

