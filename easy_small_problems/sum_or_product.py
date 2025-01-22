# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# initialize num to be used in while loop
num = 0

# make sure they enter a positive number, it'll get turned into an int even if it's not input as a whole number.  TODO: this still freaks out if it gets a value that can't be converted into an int.
while num < 1:
    num = int(input("Please enter an integer greater than 0: "))

# initialize process to be used in while loop
process = ""

# make sure they choose a valid command
while process != "s" and process != "p":
    process = (input('Enter "s" to compute the sum, or "p" to compute the product. '))

# initialize the variable that we will use as output
total = 1

#determine totals
if process == "s":
    for i in range(2, num+1):
        total += i
    print(f"The sum of integers between 1 and {num} is {total}.")
else:
    for i in range(1, num+1):
        total *= i
    print(f"The product of integers between 1 and {num} is {total}.")