array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]
array3 = []
ist = 0
for i in array1:
    for j in array2:
        if i == j:
            ist = ist + 1
    if ist == 0:
        array3.append(i)
    ist = 0
           
      
print(array3)

       
     