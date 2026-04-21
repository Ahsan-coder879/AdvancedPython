"""
In this assignment, you will design and develop a Unit Conversion System using Python.
This system will allow users to convert values from one unit to another within the same category.
In daily life, we often need to convert units such as: Length (meters to kilometers, inches to feet)Temperature
(Celsius to Fahrenheit)Weight (kilograms to grams or pounds)Time (seconds to minutes or hours)
Your program should take a value and its unit as input, then convert it into another unit based on the user’s choice.
Requirements:  Display a menu of conversion categories (e.g., Length, Temperature, Weight, Time).
Ask the user to select a category.Ask the user to input: The value to convertThe current unitThe unit to convert
into Perform the correct conversion.Display the result clearly.    Example Flow:  User selects
LengthInputs: 1000 metersChooses to convert into kilometersOutput: 1 kilometer
"""
import random

print("\n=====Rock, Paper, Scissors=====")
print("Enter: 1 for Rock, 2 for Paper, 3 for Scissors (or 0 to Exit)")

while True:
    user_input = input("\nYour Turn: ")
    if user_input == "0":
        print("Game Quit!.")
        break
    if user_input not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, 3, or 0.")
        continue
    userChoice = int(user_input)
    botChoice = random.randint(1, 3)
    rps = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {rps[userChoice]}")
    print(f"Bot chose: {rps[botChoice]}")
    if userChoice == botChoice:
        print("Result: Draw!")
    elif userChoice == 1:
        if botChoice == 3:
            print("Result: You Win!")
        else:
            print("Result: You Lose!")
    elif userChoice == 2:
        if botChoice == 1:
            print("Result: You Win!")
        else:
            print("Result: You Lose!")
    elif userChoice == 3:
        if botChoice == 2:
            print("Result: You Win!")
        else:
            print("Result: You Lose!")