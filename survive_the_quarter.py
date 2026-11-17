
# SURVIVE THE QUARTER - CROISSANT ROCKET
# Name: Assya Yuceer
# Group: A
#
# FEATURE CHOSEN: Streak bonus
# Three reputation gains in a row give an extra 500 EUR.
#
# 1. INPUT:
# The CSV file contains 14 columns with scenarios,
# three options, budget changes, reputation changes and feedback.
#
# 2. PROCESS:
# Load scenarios, shuffle them, and play 10 games.
# Each game has up to 10 days.
# The player chooses A, B or C each day.
# Budget and reputation are updated after each choice.
#
# 3. OUTPUT:
# Final budget, reputation, score, title,
# best move and worst move.
# One result is saved to results.csv after each game.
#
# 4. POSSIBLE ERRORS:
# Invalid choices are requested again.
# Missing CSV files produce an error message.
# Budget or reputation reaching zero ends the game.
# Text entered instead of numeric CSV values must be corrected.


import csv
import random
import os
from datetime import datetime


# FUNCTION 1: Load all scenarios from the CSV file

def load_scenarios(filename):

    scenarios = []

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:

        reader = csv.DictReader(file)

        for row in reader:

            scenario = {
                "ID": int(row["ID"]),
                "Scenario": row["Scenario"],

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

            scenarios.append(scenario)

    return scenarios


# FUNCTION 2: Ask the player to choose an option

def get_player_choice(scenario):

    print("\n" + scenario["Scenario"])

    print("A:", scenario["Options"]["A"][0])
    print("B:", scenario["Options"]["B"][0])
    print("C:", scenario["Options"]["C"][0])

    choice = input("Your choice (A, B or C): ").strip().upper()

    while choice not in ["A", "B", "C"]:

        print("Please type A, B or C.")
        choice = input("Your choice: ").strip().upper()

    return scenario["Options"][choice]


# FUNCTION 3: Apply the selected option

def apply_choice(option):

    option_text, budget_change, reputation_change, feedback = option

    return budget_change, reputation_change


# FUNCTION 4: Determine the player's final title

def get_title(score):

    if score < 95:
        return "Eternal Intern"

    elif score < 120:
        return "Growth Hacker"

    elif score < 140:
        return "CMO Material"

    else:
        return "Viral Legend"


# FUNCTION 5: Save the result to results.csv

def save_result(player_name, budget, reputation, title):

    filename = "results.csv"

    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

    with open(filename, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Create the header only if the file is new or empty

        if not file_exists:

            writer.writerow([
                "Name",
                "Budget",
                "Reputation",
                "Title",
                "Date"
            ])

        writer.writerow([
            player_name,
            budget,
            reputation,
            title,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])


# FUNCTION 6: Play one complete game of 10 days

def play_one_game(player_name, scenarios, game_number):

    budget = 10000
    reputation = 50

    history = []

    reputation_streak = 0

    # Shuffle the scenarios for this game

    daily_scenarios = scenarios.copy()

    random.shuffle(daily_scenarios)

    selected_scenarios = daily_scenarios[:10]

    print("\n================================")
    print("GAME", game_number, "OF 10")
    print("================================")

    # Play 10 days, unless the player gets fired

    for day, scenario in enumerate(selected_scenarios, start=1):

        print("\n--- DAY", day, "---")

        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")

        # Ask the player to choose

        result = get_player_choice(scenario)

        # Unpack the selected option

        option_text, budget_change, reputation_change, feedback = result

        # Apply the selected choice

        budget_change, reputation_change = apply_choice(result)

        budget = budget + budget_change

        reputation = reputation + reputation_change

        # Reputation cannot go above 100

        reputation = min(reputation, 100)

        # Display the feedback

        print("\n", feedback)

        print("Budget change:", budget_change, "EUR")
        print("Reputation change:", reputation_change)

        # Keep a history of each day's decision

        history.append((reputation_change, day, option_text))

        # FEATURE: Three reputation gains in a row = 500 EUR bonus

        if reputation_change > 0:

            reputation_streak = reputation_streak + 1

        else:

            reputation_streak = 0

        if reputation_streak == 3:

            budget = budget + 500

            print("STREAK BONUS! You received 500 EUR!")

            reputation_streak = 0

        # Display the updated gauges

        print("\nUpdated budget:", budget, "EUR")
        print("Updated reputation:", reputation, "/100")

        # Check if the player has been fired

        if budget <= 0 or reputation <= 0:

            print("\nGAME OVER! You have been fired.")

            if budget <= 0 and reputation <= 0:
                print("Reason: Both budget and reputation reached zero or less.")

            elif budget <= 0:
                print("Reason: Your budget reached zero or less.")

            else:
                print("Reason: Your reputation reached zero or less.")

            break

    # FINAL RESULTS OF THIS GAME

    print("\n================================")
    print("GAME", game_number, "- FINAL RESULTS")
    print("================================")

    print("Player:", player_name)
    print("Final budget:", budget, "EUR")
    print("Final reputation:", reputation, "/100")

    # Determine if the player survived

    if budget <= 0 or reputation <= 0:

        title = "Fired"

        print("Your final result: FIRED")

    else:

        score = reputation + budget // 200

        title = get_title(score)

        print("Quarter survived!")
        print("Final score:", score)
        print("Your title:", title)

    # Find the best and worst decisions

    if len(history) > 0:

        best_move = max(history)
        worst_move = min(history)

        print("\nBest move:")
        print("Day", best_move[1], "-", best_move[2])
        print("Reputation change:", best_move[0])

        print("\nWorst move:")
        print("Day", worst_move[1], "-", worst_move[2])
        print("Reputation change:", worst_move[0])

    # Automatically save this game's result

    save_result(player_name, budget, reputation, title)

    print("\nGame", game_number, "saved to results.csv!")


# MAIN PROGRAM

def main():

    try:

        # Load the CSV scenarios

        scenarios = load_scenarios("scenarios_A.csv")

        print("Total scenarios loaded:", len(scenarios))

        # Ask for the player's name

        player_name = input("\nWhat is your name? ")

        print("\nWelcome to Croissant Rocket,", player_name, "!")

        print("\nYou will play 10 games.")
        print("Each game has up to 10 days.")
        print("Good luck!")

        # Play 10 separate games

        for game_number in range(1, 11):

            play_one_game(player_name, scenarios, game_number)

        # End of tournament

        print("\n================================")
        print("TOURNAMENT COMPLETED!")
        print("================================")

        print("You have played 10 games.")

        print("All your results have been saved to results.csv.")

    except FileNotFoundError:

        print("Error: scenarios_A.csv could not be found.")

        print("Please check that the CSV file is in the same folder as your Python file.")

    except (KeyError, ValueError) as error:

        print("There is a problem with the CSV file:", error)


# Start the program

if __name__ == "__main__":

    main()
