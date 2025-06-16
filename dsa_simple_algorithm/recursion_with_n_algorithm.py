"""
Finding the n th Fibonacci number using recursion.
"""

def fibonacci(number: int):
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(19))
