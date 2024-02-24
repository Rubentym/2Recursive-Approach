def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
number = 5
fact = factorial_recursive(number)
print("Factorial of", number, "is", fact)
