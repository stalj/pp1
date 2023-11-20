import matplotlib.pyplot as plt

x = list(range(-100, 101))
y = [((n**2) - 3) for n in x]
print(y)
# Plot the graph
plt.plot(x, y)
plt.title('Graph of the function f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()