x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x > 0 and y > 0:
    print(f"P({x},{y}) is in first quadrant")
elif x < 0 and y > 0:
    print(f"P({x},{y}) is in second quadrant")
elif x < 0 and y > 0:
    print(f"P({x},{y}) is in third quadrant")
else:
    print(f"P({x},{y}) is in fourth quadrant")