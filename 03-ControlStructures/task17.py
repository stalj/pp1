x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x>0 and y>0:
    print(f"P({x},{y}) is in first quadrant of the coordinate system")
elif x<0 and y>0:
     print(f"P({x},{y}) is in second quadrant of the coordinate system")
elif x<0 and y<0:
     print(f"P({x},{y}) is in third quadrant of the coordinate system")
else:
     print(f"P({x},{y}) is in fourth quadrant of the coordinate system")
