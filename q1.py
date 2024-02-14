def is_prime(num):
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """Returns a list containing all prime numbers between 2 and n."""
    return [num for num in range(2, n + 1) if is_prime(num)]

# Example usage:
n = 20
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")


# - Can you avoid a function call?
# No, I could not avoid the function call or the helper function as it was required to check if the number that was choosen is prime number or not.

# - Can you avoid the Loop?
# No, It is not completely possible to avoid the loop as it will help to check it the number is prime or not by using the divisibility rule, so we need some type of iteration to check the numbers.

# - Can you avoid repetive code?
# There is no repetive code here.

# - Do you understand each and every line of your code?
# Yes, I did understand each and every line of my code.
