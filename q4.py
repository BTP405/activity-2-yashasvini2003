def statistics_decorator(func):
    def wrapper(numbers):
        count = len(numbers)
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)

        print(f"Numbers: {numbers}")
        print(f"Count: {count}")
        print(f"Average: {average:.2f}")
        print(f"Maximum: {maximum}")

        func(numbers)

    return wrapper

@statistics_decorator
def process_numbers(numbers):
    # Additional processing logic can be added here if needed
    pass

def printStats(t):
    """Reads lines of numbers from the file 't' and prints statistics."""
    with open(t, 'r') as file:
        for line in file:
            numbers = [float(num) for num in line.split()]
            process_numbers(numbers)

# Example usage:
file_path = 'sample_numbers.txt'
printStats(file_path)
