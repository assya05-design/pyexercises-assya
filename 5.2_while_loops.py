"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Answers entered by the user.
# 2. Process: Repeat the question until the correct answer is given.
# 3. Out: Feedback after each attempt and a final summary.
# 4. My stop condition, my attempt limit, my summary:


# Your code below
attempts = 0
max_attempts = 5
success = False

while attempts < max_attempts and not success:
    answer = input("Is the fashion campaign ready? Type yes: ")
    attempts += 1

    if answer.strip().lower() == "yes":
        success = True
        print("Great! The campaign is ready.")
    else:
        print("Not yet. Please try again.")

print("Attempts:", attempts)

if success:
    print("Result: Success!")
else:
    print("Result: Maximum attempts reached.")
