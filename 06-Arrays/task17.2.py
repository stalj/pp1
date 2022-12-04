def f():
    array = [8,5,2,1,9]
    s1 = "Array: "
    s2 = ''
    s5=''
    for i in range(int(len(array))):
        s2 =s2 + " " +str(array[i])
    s3= "\n"
    s4="2nd power array: "
    for i in range(int(len(array))):
        s5 = s5 + " "+str(array[i]*array[i])  
    
    return s1 + s2 +s3 + s4+ s5

print(f())

