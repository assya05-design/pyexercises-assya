"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: Campaign name, brand, budget, city and marketing channel entered by the user.
# 2. Process: The program collects the information, checks that the budget is a valid positive number, and saves the data into a CSV file without deleting previous entries.
# 3. Out, file name and columns:
# File name: fashion_campaigns.csv
# Columns: Campaign, Brand, Budget, City, Marketing_Channel.
# 4. Why these columns, and what this file is for: These columns help organise fashion campaign information. The file can be used to compare campaign budgets, brands,locations and marketing channels, and analyse up to 200 campaigns.


# Your code below
import csv
import os

# Name of the CSV file
filename = "fashion_campaigns.csv"

# Define the columns
columns = ["Campaign", "Brand", "Budget", "City", "Marketing_Channel"]

# Ask the user for campaign information
campaign = input("Enter campaign name: ")
brand = input("Enter brand: ")

# Make sure the budget is a valid positive number
while True:
    try:
        budget = float(input("Enter campaign budget (€): "))
        if budget > 0:
            break
        else:
            print("Please enter a positive budget.")
    except ValueError:
        print("Please enter a valid number.")

city = input("Enter city: ")
channel = input("Enter marketing channel: ")

# Check if the file already exists
file_exists = os.path.exists(filename)

# Open the file in append mode
with open(filename, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)

    # Write the header only if the file is new or empty
    if not file_exists or os.path.getsize(filename) == 0:
        writer.writeheader()

    # Save the campaign information
    writer.writerow({
        "Campaign": campaign,
        "Brand": brand,
        "Budget": budget,
        "City": city,
        "Marketing_Channel": channel
    })

print("Campaign successfully saved!")
