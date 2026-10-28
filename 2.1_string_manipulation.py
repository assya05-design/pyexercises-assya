"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence entered by the user
# 2. Process: Apply four different string methods to the sentence
# 3. Out: Four different versions of the sentence.
# 4. My four transformations, and when each is useful:
# - Lowercase: useful for comparing text without worrying about capitals.
# - Uppercase: useful for titles or labels.
# - Capitalize: useful for making the first letter a capital.
# - Strip: useful for removing spaces at the beginning and end.

# Your code below

sentence = input("Enter a sentence:")
print("Enter a sentence")

#This sentence will appear in lowercase
print("lowercase:", sentence.lower())

#This sentence will appear in uppercase
print("uppercase:", sentence.upper())

#This sentence will appear in catitalized
print("capitalize:", sentence.capitalize())

#This sentence will appear stripped
print("strip:", sentence.strip())