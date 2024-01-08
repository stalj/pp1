import math
import matplotlib.pyplot as plt
x = list(range(0, 360))
y = [math.sin(math.radians(n)) for n in x]
plt.plot(x, y)
plt.title('Graph of the function f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()