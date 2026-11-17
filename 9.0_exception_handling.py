"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a number.
# 2. Process: The program divides 100 by the number entered. It checks whether the input is a valid number and whether it is zero.
# 3. Out: The result of the division, or an error message if the input is invalid.
# 4. The two failures, and whether they deserve the same message: 
    #ZeroDivisionError: when the user enters zero.
    #ValueError: when the user enters text that cannot be converted into a number.
    #They should have different messages because the problems are different.
    # Catching each error separately is better because it helps the user understand exactly what went wrong.


# Your code below
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user_input = input("Enter a number to divide 100 by: ")

    try:
        number = float(user_input)

        result = 100 / number

        print("The result is:", result)
        break

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

    except ValueError:
        if user_input == "":
            print("Error: You entered nothing. Please enter a number.")
        else:
            print("Error: Invalid input. Please enter a valid number.")

    attempts = attempts + 1

else:
    print("You have reached the maximum number of attempts.")
    
print("Program finished.")
