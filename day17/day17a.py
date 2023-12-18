import matplotlib.pyplot as plt
import numpy as np

with open("day17.txt", "r") as file:
    lines = file.readlines()
    fixed_lines = []
    for line in lines:
        fixed_lines.append([int(char) for char in line.strip()])
    #fixed_lines = [list(map(int, line.strip())) for line in lines]


    print(fixed_lines)

    # Convert the data to a NumPy array of integers
    data_array = np.array(fixed_lines, dtype=int)

    # Set up a gradient from 1 to 10
    cmap = plt.cm.get_cmap('viridis', 10)

    # Plot the grid
    plt.imshow(data_array, cmap=cmap, interpolation='nearest')

    # Add colorbar for the gradient
    cbar = plt.colorbar(ticks=range(1, 11))
    cbar.set_label('Gradient Value')

    # Save the plot to a file
    plt.savefig('output_plot.png')