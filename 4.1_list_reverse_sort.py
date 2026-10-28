"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original list created in exercise 4.0.
# 2. Process: Display the list in four different orders.
# 3. Out: The original list and four different orderings.
# 4. My four orders, and which ones modify the original: I chose ascending, descending, reversed, and numerical order, sort() modifies the original list.


# Your code below
# 4.0 Original List
budgets = [750,300,1009, 470,678, 450, 200, 860]
print("original list:", budgets)

# 1. Sorted from smallest to largest
print("Ascending:", sorted(budgets))

# 2. Sorted from largest to smallest
print("Descending:", sorted(budgets,reverse=True))

# 3. Reversed order
print ("Reverse:", list(reversed(budgets)))

# 4. Sort the original list in place
budgets_copy = budgets.copy()
budgets_copy.sort()
print("Sorted copy:", budgets_copy)

# Prove the original list has changed
print("original list at the end:", budgets)
