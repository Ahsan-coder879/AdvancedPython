"""
# 1. The print() Function
# Focus: String manipulation and formatting.

# 1. The Multi-Line Story: Print a short story (3 lines) using only one print() statement

multi = input("Enter Line1: ")
line = input("Enter Line2: ")
story = input("Enter Line3: ")

print(f" {multi}\n" f" {line}\n" f" {story}")

#2. The Border: Print the word "PYTHON" surrounded by a box made of asterisks (*).


2. The input() Function
Focus: Type casting and user interaction.

#1. The Greeter: Ask for a name and a favorite color, then print: "Hi [Name], [Color] looks great on you!"

name = input("Enter Name: ")
fav_color = input("Enter Favorite Color: ")
print(f"Hi {name}, {fav_color} Color looks great on you!")
"""
from numpy.ma.core import reshape

#2. The Age Gap: Ask for the user's age and print how old they will be in the year 2050.
"""
age = int(input("Enter Age: "))
current_year = int(input("Enter Current Year: "))
future_Year = int(input("Enter Future Year to calculate your Age: "))
print(f"You are {age+(future_Year - current_year)} years old in {future_Year}.")

#3. The Multiplier: Ask for two numbers, multiply them, and print the result. (Watch out for string vs. integer errors!)
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
multiply = num1 * num2
print(f"Multiply {num1} by {num2} = {multiply}")

#4. The Repeater: Ask for a word and a number, then print that word as many times as the number specifies.
word = str(input("Enter Word: "))
num = int(input("Enter Number: "))
print((word+"\n")*num)

#5. The Bill Splitter: Ask for a total bill amount and the number of people. Print how much each person owes.
total_bill = int(input("Enter Total Bill: "))
num_people = int(input("Enter Number of People: "))
splitt = total_bill // num_people
print(float(splitt))
"""
import numpy as np
matricDimention = (2,3,2,6,4)
arr =np.array(range(288))