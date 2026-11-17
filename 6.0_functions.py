"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight marketing campaign budgets.
# 2. Process:Calculate the total budget of the list.
# 3. Out: Return the total budget as a number.
# 4. My function name, and why return rather than print: calculate_total. The name explains what the function does. Return sends the result back so it can be resued.
#Print only displays information on the screen.

# Your code below
# Original list from Exercise 4.0
budgets = [750, 300, 1009, 470, 678, 450, 200, 860]


# Create a function to calculate the total budget
def calculate_total(budgets):
    return sum(budgets)


# Create three different lists using the original budgets
campaign_1 = budgets[:3]
campaign_2 = budgets[3:6]
campaign_3 = budgets[6:]


# Call the function three times
result_1 = calculate_total(campaign_1)
result_2 = calculate_total(campaign_2)
result_3 = calculate_total(campaign_3)


# Display the three results
print("Campaign 1 total:", result_1)
print("Campaign 2 total:", result_2)
print("Campaign 3 total:", result_3)


# Test the function with an empty list
empty_list = []
print("Empty list total:", calculate_total(empty_list))

# An empty list returns 0, which is acceptable.
