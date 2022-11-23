array1 = [9, 4, 5, 8, 10]
array2 = [1, 2, 3]
 
# printing original lists
print("Original list : " + str(array1))
print("Original sub list : " + str(array2))
 
# using all() to
# check subset of list
flag = 0
if(all(x in array1 for x in array2)):
    flag = 1
 
# printing result
if (flag):
    print("Yes, array is subset of other.")
else:
    print("No, array is not subset of other.")