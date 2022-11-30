def f(dictionary,x,y):
    sum=0
    for i in dictionary.values():
        for j in i:
            if j in range(x,y+1):
                sum=sum+j
                #print(j)
    print(sum)


f({"arr1":[4,5,6], 
"arr2":[7,5]}, 5, 6) 

f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) 