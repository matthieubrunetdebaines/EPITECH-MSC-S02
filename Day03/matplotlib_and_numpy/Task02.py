import matplotlib.pyplot as plt

x = [ 0, 1, 2, 3 ]
y = [12, 32, 42, 52]

plt.scatter(x, y, label="Data Points")

plt.xlabel("X-Axis")
plt.xlabel("Y-Axis")
plt.title("Scatter Plot of Points")

plt.grid(True)

plt.legend()

plt.show()
