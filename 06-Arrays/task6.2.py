array = [2,3,7,5,4]
#display the array
print(array)
#b.	number of elements
print(len(array))
#c.	first value
print(array[0])
#d.	second value
print(array[1])
#e.	last value
print(array[-1])
#f.	last but one value
print(array[4])
#g.	sum of the first and last value
print(array[0] + array[-1])
#h.	middle value
middle = int(len(array))
print(array[int(middle/2)])
#i.	all array values separated by a single space (use a loop statement)
for i in array:
    print(i , end = " ")
print()
#j.	all array values from first to middle separated by a single space (use a loop statement)
for i in range(int(len(array)/2 +1)):
    print(array[i], end = " ")
