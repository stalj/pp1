array = [-15, 8, -31, 47, -2, 19]

max_x=array[0]
min_x=array[0]

for i in array:
    if i>= max_x:
        max_x = i
    elif i <= min_x:
        min_x = i
    
print(f"Maximum is {max_x}, and minimum is {min_x}")


