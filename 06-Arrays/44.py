import matplotlib.pyplot as plt

x = []
y = []

for num in range(-100,101):
    x. append(num)

for num in x:
    y.append(num**2 - 3)

plt.plot(x,y)
plt.show()