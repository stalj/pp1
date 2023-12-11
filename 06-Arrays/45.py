import matplotlib.pyplot as plt
import math

x = []
y = []

for num in range(0,361):
    x. append(num)

for num in x:
    y.append(math.sin(num))

plt.plot(x,y)
plt.show()