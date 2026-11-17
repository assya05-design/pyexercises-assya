"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in? Two text values: "Paris" and "paris".
    2. What happens to it? Python compares the two strings using comparison operators. It checks equality, inequality and alphabetical order. It then combines the comparison results using and, or and not.
    3. What comes out? A readable table showing all comparison results and the logical combinations of those results.
    4. Which two values did you pick, and which comparison result surprised you? I picked "Paris" and "paris". The surprising result is that "Paris" is smaller than "paris". This is because Python is case-sensitive and uppercase letters are ordered before lowercase letters.

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# STEP 1: Choose two values
value1 = "Paris"
value2 = "paris"

# STEP 2: Display the two values
print("COMPARING TWO VALUES")
print("--------------------")
print("First value:", value1)
print("Second value:", value2)

# STEP 3: Compare the two values
results = {
    "value1 == value2": value1 == value2,
    "value1 != value2": value1 != value2,
    "value1 < value2": value1 < value2,
    "value1 <= value2": value1 <= value2,
    "value1 > value2": value1 > value2,
    "value1 >= value2": value1 >= value2
}

# STEP 4: Display comparison results in a readable table
print("\nCOMPARISON RESULTS")
print("------------------")
print(f"{'Comparison':<25} {'Result'}")
print("-" * 35)

for comparison, result in results.items():
    print(f"{comparison:<25} {result}")

# STEP 5: Display logical combinations
print("\nLOGICAL COMBINATIONS")
print("--------------------")

print(f"{'Expression':<45} {'Result'}")
print("-" * 55)

# Combine the first two comparison results
equal_result = results["value1 == value2"]
not_equal_result = results["value1 != value2"]

print(f"{'Equality AND inequality':<45} {equal_result and not_equal_result}")
print(f"{'Equality OR inequality':<45} {equal_result or not_equal_result}")
print(f"{'NOT equality':<45} {not equal_result}")
print(f"{'NOT inequality':<45} {not not_equal_result}")

# Combine the alphabetical comparison results
less_result = results["value1 < value2"]
greater_result = results["value1 > value2"]

print(f"{'Less than AND greater than':<45} {less_result and greater_result}")
print(f"{'Less than OR greater than':<45} {less_result or greater_result}")
print(f"{'NOT less than':<45} {not less_result}")
print(f"{'NOT greater than':<45} {not greater_result}")

print("\nEND OF PROGRAM")