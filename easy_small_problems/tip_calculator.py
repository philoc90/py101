# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.


# Get user input, turn into a float
bill = float(input("How much was the bill? "))
percent = float(input("What % tip would you like to give? "))
# calculate tip
tip = bill * (percent * 0.01)
print(f"The tip is ${tip:.2f}.")
print(f"Your grand total is ${(bill + tip):.2f}.")