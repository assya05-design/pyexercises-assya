"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of fashion marketing campaigns budget. 
# 2. Process: Sort the list and calculate the total budget. 
# 3. Out: The whole list, one item, the sorted list, and the total.
# 4. What my list is about, and what I computed from it: y list is about campaign budgets. The total shows
# the overall budget needed for all eight campaigns.


# Your code below
# Create a list with eight campaign budgets
budgets = [750,300,1009, 470,678, 450, 200, 860]

# Display the whole list
print("All budgets:", budgets)

# Display one item from the list
print("One item of your choice:", budgets[3])

# Display the list sorted from smallest to largest
print ("Sorted budgets:", sorted(budgets))

# Calculate and display the total
print ("Total budgets:", sum(budgets))