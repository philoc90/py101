# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.
import random


# Modify this program to ask for a name, then print the age for that person. For an extra challenge, use "Teddy" as the name if no name is entered.
def greeting(name):
    if not name:
        name = "Teddy"
    print(f"{name} is {random.randrange(20, 101)} years old!")

greeting(input("What is your name? "))