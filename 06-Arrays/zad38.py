def create_2d_arr(x,y):
    a = []
    b = []
    for i in range (0, x):
        for j in range (0, y):
            b.append(0)
        a.append(b)
        b = []
    return(a)
print(create_2d_arr(2,2))