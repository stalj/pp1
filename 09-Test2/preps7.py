def f4(d):
    suma=0
    for i in d:
        for j in d[i]:
            #if j >=5 and j<=10:
            if j in range(5,11):
                suma=suma+j
    return suma
print(f4({"arr1": [2,6,5],"arr2":[7,1],"arr3":[2,9,8,1]}))