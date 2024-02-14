import numpy as np
import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Define ranges in 10 cm intervals
    ranges = np.arange(0, 60, 10)
    count = np.zeros(len(ranges) - 1)  # Initialize count for each range
    
    # Read data from file
    with open(t, 'r') as file:
        snowfall_data = np.array([int(line.strip()) for line in file])
    
    # Count occurrences in each range
    count, _ = np.histogram(snowfall_data, bins=ranges)
    
    # Plot the bar chart
    plt.bar([f"{ranges[i]}-{ranges[i+1]}" for i in range(len(ranges) - 1)], count, color='skyblue')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.show()
    plt.savefig('snowfall.png')

# Example usage:
graphSnowfall('snowfall-data.txt')
