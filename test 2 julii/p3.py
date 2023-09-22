def f(array):
    result=[]
    suma=0
    for i in range (len(array[0])):
        for j in range (len(array)):
            suma+=array[j][i]
        result.append(suma)
        suma=0  

    najwieksza=result[0]
    for r in result:
        if r> najwieksza:
            najwieksza=r
    
    z=result.index(najwieksza)
    return z





f([[6,9],[9,5]])

