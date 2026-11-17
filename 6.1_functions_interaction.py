"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight fashion campaign budgets.
# 2. Process, function by function: Calculate the total, average and highest budget.
# 3. Out: Display the three results.
# 4. The question my fourth function answers: The fourth function combines the three calculations.


# Your code below
# Original list from Exercise 4.0
budgets = [750, 300, 1009, 470, 678, 450, 200, 860]


# FUNCTION 1: Calculate the total
def calculate_total(budgets):
    return sum(budgets)


# FUNCTION 2: Calculate the average
def calculate_average(budgets):
    if len(budgets) == 0:
        return 0
    return sum(budgets) / len(budgets)


# FUNCTION 3: Find the highest budget
def find_highest(budgets):
    if len(budgets) == 0:
        return None
    return max(budgets)


# FUNCTION 4: Combine the three functions
def budget_summary(budgets):
    total = calculate_total(budgets)
    average = calculate_average(budgets)
    highest = find_highest(budgets)

    return total, average, highest


# TEST EACH FUNCTION INDIVIDUALLY

# Test 1: Input [100, 200, 300]
# Expected output: 600
print("Test total:", calculate_total([100, 200, 300]))

# Test 2: Input [100, 200, 300]
# Expected output: 200
print("Test average:", calculate_average([100, 200, 300]))

# Test 3: Input [100, 200, 300]
# Expected output: 300
print("Test highest:", find_highest([100, 200, 300]))


# USE THE FOURTH FUNCTION WITH OUR ORIGINAL LIST
total, average, highest = budget_summary(budgets)

print("\nFASHION CAMPAIGN BUDGET SUMMARY")
print("Original budgets:", budgets)
print("Total budget:", total)
print("Average budget:", round(average, 2))
print("Highest budget:", highest)