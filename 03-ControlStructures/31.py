# Which quadrant I-IV
# or on which axis
# or in (0,0)

x = int(input("x = "))
y = int(input("y = "))

# I quad
if x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the 1st quad")

# II quad
if x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the 2nd quad")

# III quad
if x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the 3rd quad")

# IV quad
if x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the 4th quad")

# Only X axis
if x < 0 and y == 0:
    print(f"Point P({x},{y}) is located on the X axis")
elif x > 0 and y == 0:
    print(f"Point P({x},{y}) is located on the X axis")

# Only Y axis
if y < 0 and x == 0:
    print(f"Point P({x},{y}) is located on the Y axis")
elif y > 0 and x == 0:
    print(f"Point P({x},{y}) is located on the Y axis")

# 0,0
if x == 0 and y == 0:
    print(f"Point P({x},{y}) is located on the (0,0) position")
