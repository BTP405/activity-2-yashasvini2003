   # Helper function to check if a number is prime.
def is_prime(num):
    # If the number is less than 2, it's not prime
    if num < 2:
        return False
    # Loop through potential divisors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        # If the number is divisible by any number in this range, it's not prime
        if num % i == 0:
            return False
    # If the number is not divisible by any number in the range, it's prime
    return True

# Returns a list containing all prime numbers between 2 and n.
def getPrimeNumbers(n):
    # Iterate through numbers from 2 to n (inclusive) and filter out non-prime numbers
    return [num for num in range(2, n + 1) if is_prime(num)]

# Example usage:
n = 20
# Get the prime numbers up to n
prime_numbers = getPrimeNumbers(n)
# Print the prime numbers between 2 and n
print(f"Prime numbers between 2 and {n}: {prime_numbers}")



# - Can you avoid a function call?
# No, I could not avoid the function call or the helper function as it was required to check if the number that was choosen is prime number or not.

# - Can you avoid the Loop?
# No, It is not completely possible to avoid the loop as it will help to check it the number is prime or not by using the divisibility rule, so we need some type of iteration to check the numbers.

# - Can you avoid repetive code?
# There is no repetive code here.

# - Do you understand each and every line of your code?
# Yes, I did understand each and every line of my code.
