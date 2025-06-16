"""
An implementation of the Fibonacci algorithm above using a for loop.
"""

previous_two = 0
previous_one = 1

print(f"{previous_two}, {previous_one} fibonacci numbers.")

for _ in range(18):
    new_fibo = previous_one + previous_two
    print(f"{new_fibo} new fibonacci number")
    previous_two = previous_one
    previous_one = new_fibo
