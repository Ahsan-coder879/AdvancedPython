# Create banking System
# Ask user to Create Account or Check or withDraw or deposit
# Use while true for this process
# Lets say user created account = 5000
# Dictionary Example = {"UserNames":[a,b,c,d,e],"Age":[1,2,3,4],"Balance":[1000,2000,3000,4000]
#Create a csv and store data in therep
"""
Create a Simple Banking System in Python that stores account data in a CSV file using the Pandas library. The program should be menu-driven and continuously run until the user chooses to exit. The CSV file should contain the columns AccountNumber, Name, and Balance. The program must support the following operations:
	1.	Create Account – Ask the user for account number, customer name, and initial balance, then store the record in the CSV file.
	2.	Deposit Money – Ask for account number and deposit amount, find the account, and increase the balance.
	3.	Withdraw Money – Ask for account number and withdrawal amount, check if the account has sufficient balance, and subtract the amount if possible. If not, display “Insufficient Balance.”
	4.	Check Balance – Ask for the account number and display the current balance of that account.
	5.	Exit – Terminate the program when the user selects this option.

The program should read data from the CSV file, update it when transactions occur, and save the updated data back to the file.
"""

