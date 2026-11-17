"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in? The user enters a name, an email address and a phone number.
    2. What happens to it? The program checks each piece of information using regular expressions. It checks that all three fields follow the rules.
    3. What comes out? If all three fields are valid, the information is saved in a file. If one or more fields are invalid, the user must try again.
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.
       NAME:
- Must contain only letters and spaces.
- Must contain at least two characters.
- Cannot be empty.

EMAIL:
- Must contain text before and after @.
- Must contain a dot after @.
- Cannot contain spaces.

PHONE:
- Must contain exactly 10 digits.
- Cannot contain letters or spaces.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
import re

while True:
    print("\nPlease enter your information.")

    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")

    # Check the name
    name_valid = re.fullmatch(r"[A-Za-z ]{2,}", name) is not None

    # Check the email
    email_valid = re.fullmatch(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        email
    ) is not None

    # Check the phone number
    phone_valid = re.fullmatch(r"\d{10}", phone) is not None

    # Display validation results
    print("\nVALIDATION RESULTS")

    if name_valid:
        print("Name: Valid")
    else:
        print("Name: Invalid. Use at least two letters and spaces only.")

    if email_valid:
        print("Email: Valid")
    else:
        print("Email: Invalid. Enter an email such as example@gmail.com.")

    if phone_valid:
        print("Phone: Valid")
    else:
        print("Phone: Invalid. Enter exactly 10 digits.")

    # Save only if all three fields are valid
    if name_valid and email_valid and phone_valid:

        with open("valid_information.txt", "a", encoding="utf-8") as file:
            file.write(name + "," + email + "," + phone + "\n")

        print("\nAll information is valid!")
        print("Your information has been saved.")
        break

    else:
        print("\nSome information is incorrect. Please try again.")

print("Program finished.")
