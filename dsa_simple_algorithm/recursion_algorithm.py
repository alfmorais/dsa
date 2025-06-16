"""
An implementation of the Fibonacci algorithm above using recursion.
"""
previous_two = 0
previous_one = 1
count = 2

def fibonacci(previous_one: int, previous_two: int):
    global count

    if count <= 19:
        new_fibo = previous_one + previous_two
        print(f"{new_fibo} new fibonacci number")
        previous_two = previous_one
        previous_one = new_fibo
        count += 1
        fibonacci(previous_one, previous_two)
    else:
        return

fibonacci(previous_one, previous_two)
