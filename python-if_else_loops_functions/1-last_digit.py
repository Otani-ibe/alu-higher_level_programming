#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit using modulo operation
last_digit = abs(number) % 10

# Print the formatted output
print(f"Thestring Last digit of {number} is {last_digit}, ", end="")
if last_digit > 5:
    print(f"and is greater than 5")
elif last_digit == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")

