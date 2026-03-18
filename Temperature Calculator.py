"""
Temperature Calculator
🌡️ Problem: All Temperature CalculatorTemperature is a very important measurement used in everyday life,
science, and technology. It tells us how hot or cold something is. Different countries and systems use
different units to measure temperature, such as Celsius, Fahrenheit, and Kelvin.Because of these different
units, people often need to convert temperature from one unit to another. For example, weather reports,
scientific experiments, and engineering systems may require temperature in a specific unit.🎯
ObjectiveYour task is to create a Python program that works as a Temperature Calculator. The program
should help users easily convert temperature values between different units.🧩 Problem DescriptionThe
program should start by displaying a menu with different conversion options. The user will choose one
option depending on the type of temperature they want to convert.After selecting an option, the program
should:Ask the user to enter a temperature valueConvert that value into the other temperature unitsDisplay
the converted results clearly on the screenFor example:If the user enters temperature in Celsius, the program
should convert it into Fahrenheit and KelvinIf the user enters temperature in Fahrenheit, it should convert it
into Celsius and KelvinIf the user enters temperature in Kelvin, it should convert it into Celsius and Fahrenheit📋
RequirementsThe program must display a menu with at least three optionsThe user should be able to select an option
using inputThe program should take temperature input from the userIt should perform the correct conversion based on
the selected optionThe results should be printed in a clear and readable formatIf the user enters an invalid option,
the program should show an error message🧠 Expected Learning OutcomesBy completing this problem,
students will:Understand the concept of temperature conversionLearn how to take input from usersPractice
using conditional statementsImprove problem-solving and programming skills
"""



while True:
    print("\n=================")
    print("ALL TEMPERATURE CALCULATOR MENU: ")
    print("=======================")
    print("1: Celsius to Fahrenheit & Kelvin")
    print("2: Fahrenheit to Celsius & Kelvin")
    print("3: Kelvin to Celsius & Fahrenheit")
    print("4: Exit Program")

    choice = input("\nSelect an option (1-4): ")


    if choice == "4":
        print("signing out")
        break

    if choice in ["1", "2", "3"]:
            temp = float(input("Enter the temperature value: "))

            if choice == "1":
                f = (temp * 9 / 5) + 32
                k = temp + 273.15
                print(f"\n {temp}°C is equal to {f:.2f}°F and {k:.2f}K")

            elif choice == "2":
                c = (temp - 32) * 5 / 9
                k = c + 273.15
                print(f"\n {temp}°F is equal to {c:.2f}°C and {k:.2f}K")

            elif choice == "3":
                c = temp - 273.15
                f = (c * 9 / 5) + 32
                print(f"\n {temp}K is equal to {c:.2f}°C and {f:.2f}°F")

    else:
        print("Error: Invalid option. Please select 1, 2, 3, or 4.")

