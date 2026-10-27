"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers entered by the user
# 2. Process: Addition, Substraction, Multiplication, Division
# 3. Out: The results of the four operations
# 4. What happens when the second number is zero, and why: Python emits an error message, because a division by 0 is undefined. Therefore we need to use an "if ... else" formula.


# Your code below
number1 = float(input("Enter the first nummber:"))
number2 = float(input("Enter the second number:"))

print(number1, number2)

# sum of the numbers
sum = number1 + number2
print("The sum of two numbers if:", sum)

# substraction of the numbers
substraction = number1 - number2
print("The substraction of the two numbers if:", substraction)

#multiplication of the numbers
multiplication = number1 * number2
print("The multiplication of the two numbers if:", multiplication)

# division of the numbers
if number2 !=0:
    division = number1 / number2
    printrint("The division of the two numbers if:", division)
else:
    print("The number2 is zero")

