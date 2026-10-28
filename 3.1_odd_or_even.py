"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A number N.
# 2. Process: Check each number to determine if it is odd or even.
# 3. Out: Whether each number is odd or even. 
# 4. What happens on 0, on a negative number, on a very large number:
# 0: Display a message asking for a positive number.
# Negative number: Display a message asking for a positive number.
# 5000: Display a message asking to input a number lower than 1000


# Your code below


# If a number is 0, negative or above 1000
n = int(input("Enter a positive number:"))
if n <= 0:
    print("Please enter a positive number.")
elif n > 1000:
    print("Number is too large. Please enter a number up to 1000.")
else:
    for number in range (1, n+1):
        if number % 2 == 0:
            print(number,"number is even")
        else:
            print(number, "is odd")
