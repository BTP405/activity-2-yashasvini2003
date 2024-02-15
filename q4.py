def statistics_decorator(func):
    # Define a decorator function that takes another function as input
    def wrapper(numbers):
        # Define a wrapper function that adds statistics functionality to the input function
        count = len(numbers)  # Count the number of elements in the input list
        total = sum(numbers)  # Calculate the sum of all elements in the input list
        average = total / count  # Calculate the average of all elements in the input list
        maximum = max(numbers)  # Find the maximum value in the input list

        # Print statistics information
        print(f"Numbers: {numbers}")  # Print the input list of numbers
        print(f"Count: {count}")  # Print the count of numbers
        print(f"Average: {average:.2f}")  # Print the average of numbers with two decimal places
        print(f"Maximum: {maximum}")  # Print the maximum number
        
        # Call the original function with the input list
        func(numbers)

    return wrapper  # Return the wrapper function

@statistics_decorator
def process_numbers(numbers):
    # Decorated function: Performs additional processing and prints statistics
    pass

def printStats(t):
    """Reads lines of numbers from the file 't' and prints statistics."""
    with open(t, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Convert each line of numbers to a list of floats
            numbers = [float(num) for num in line.split()]
            # Call the decorated function to process the list of numbers and print statistics
            process_numbers(numbers)

# Example usage:
file_path = 'sample_numbers.txt'
printStats(file_path)  # Call the printStats function with the file path to read and print statistics for each line of numbers

# - Can you avoid a function call?
# The function call is used in line 38, but the function call cannot be avoided as the code will be more difficult and complex to understand as well as it will be lengthy.

# - Can you avoid the Loop?
# There is the use of loop in line 30, the loop will help to read content of the file and process the numbers.
# We can use methods or libraries in order to avoid loops but they will much more difficult to handle as compared to loop 

# - Can you avoid repetive code?
# There is no repetive code here. If any,  then I have already removed the repetive codes to make the code understandable

# - Do you understand each and every line of your code?
# Yes, I did understand each and every line of my code.
