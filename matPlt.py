import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 12, 8, 14, 20]

# Create a line plot
plt.plot(x, y, color='blue', marker='o', linestyle='--')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
