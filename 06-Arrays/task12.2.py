array = [[2,5,4],[9,0,3]]
#a.	the array
print(array)

#b.	size of the array (number of rows and columns)
print(len(array), len(array[0]))

#c.	value 5 from the array
print(array[0][1])

#d.	value 3 from the array
print(array[1][2])

#e.	second row of the array as below:
#9 0 3
for i in array[1]:
    print(i, end = " ")
print()
#f.	all values from the array as below:
#2 5 4 
#9 0 3
for i in array:
    print(i)