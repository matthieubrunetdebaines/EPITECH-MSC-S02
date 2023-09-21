import matplotlib.pyplot as plt

def display_points_as_chart(points):
    # Unzip the list of points into separate lists of x and y coordinates
    x, y = zip(*points)

    # Create a scatter plot
    plt.scatter(x, y, label='Data Points')


    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Scatter Plot of Points')

    # Display grid lines
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage:
points = [(0, 12), (1, 32), (2, 42), (3, 52)]


display_points_as_chart(points)