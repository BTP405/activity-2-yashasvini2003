import numpy as np
import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Define ranges in 10 cm intervals
    ranges = np.arange(0, 60, 10)
    count = np.zeros(len(ranges) - 1)  # Initialize count for each range
    
    # Read data from file
    with open(t, 'r') as file:
        # Read each line from the file, convert to integer, and store in numpy array
        snowfall_data = np.array([int(line.strip()) for line in file])
    
    # Count occurrences in each range
    # Generate a histogram of the snowfall data with specified range
    count, _ = np.histogram(snowfall_data, bins=ranges)
    
    # Plot the bar chart
    plt.bar([f"{ranges[i]}-{ranges[i+1]}" for i in range(len(ranges) - 1)], count, color='skyblue')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.show()  # Display the plot
    
    # Save the plot as an image file
    plt.savefig('snowfall.png')

# Example usage:
graphSnowfall('snowfall-data.txt')

# - Can you avoid a function call?
Yes, the function graphSnowfall can be avoided and simply the range and count can be defined.

# - Can you avoid the Loop?
# No, It is not completely possible to avoid the loop as loop here is telling the extent of the range of the graph to be drawn.

# - Can you avoid repetive code?
# There is no repetive code here.

# - Do you understand each and every line of your code?
# Yes, I did understand each and every line of my code.
