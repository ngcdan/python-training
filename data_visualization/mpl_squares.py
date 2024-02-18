import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('bmh')
fig, ax = plt.subplots()

# To plot a single point, use the scatter(x, y) method.
# ax.scatter(2, 4, s=100)
# Plot input values vs output values
ax.scatter(input_values, squares, c='red', s=90)

# input values corresponding to squares (x values)
# squares (output values) corresponding to squares (y values)
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Styles available on your system
print(plt.style.available)

plt.show()
# Saving the figure
fig.savefig('squares_plot.png', bbox_inches='tight')
