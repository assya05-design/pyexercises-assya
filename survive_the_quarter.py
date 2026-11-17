import csv

with open ("scenarios_A.csv","r") as file:
    reader = csv.DictReader(file)

scenarios = []

# Open the CSV file
with open("scenarios_A.csv", "r", newline="", encoding="utf-8") as file:

    # Read the CSV using column names
    reader = csv.DictReader(file)

    # Go through each row
    for row in reader:

        # Create a dictionary for each scenario
        scenario = {
            "ID": int(row["ID"]),
            "Scenario": row["Scenario"],

            # Store the three options
            "Options": {
                "A": (
                    row["OptionA"],
                    int(row["BudgetA"]),
                    int(row["ReputationA"]),
                    row["FeedbackA"]
                ),

                "B": (
                    row["OptionB"],
                    int(row["BudgetB"]),
                    int(row["ReputationB"]),
                    row["FeedbackB"]
                ),

                "C": (
                    row["OptionC"],
                    int(row["BudgetC"]),
                    int(row["ReputationC"]),
                    row["FeedbackC"]
                )
            }
        }

        # Add the scenario to the list
        scenarios.append(scenario)


# Display the results
print("Total scenarios:", len(scenarios))
print("First scenario:", scenarios[0])
print("Last scenario:", scenarios[-1])

# Randomly select 10 scenarios
import random

selected_scenarios = random.sample(scenarios, 10)

# Display the 10 selected scenarios
print("\nYour 10 random scenarios:")

# Ask for the player's name
player_name = input("\nWhat is your name? ")

print("Welcome to Croissant Rocket,", player_name, "!")

for scenario in selected_scenarios:
    # Display the scenario
    print("\nScenario", scenario["ID"])
    print(scenario["Scenario"])

    # Display the three options
    print("A:", scenario["Options"]["A"][0])
    print("B:", scenario["Options"]["B"][0])
    print("C:", scenario["Options"]["C"][0])

    # Ask the player to choose
    choice = input("Choose A, B or C: ").upper()

    # Check if the choice is valid
    while choice not in ["A", "B", "C"]:
        print("Invalid choice. Please try again.")
        choice = input("Choose A, B or C: ").upper()

    # Retrieve the selected option
    result = scenario["Options"][choice]