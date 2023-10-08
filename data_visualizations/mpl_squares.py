import matplotlib.pyplot as plt

# Plotting a simple line graph
squares = [1, 4, 9, 16, 25]

input_values = [1, 2, 3, 4, 5]

print(f"{plt.style.available}\n")

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
ax.scatter(x_values, y_values, c='red', s=10)

# Controls the thickness of the line
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')