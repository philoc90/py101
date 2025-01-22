# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

def caps(name):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")

def no_caps(name):
    print(f"Hello, {name}.")

name = input("What is your name? ")

if name[-1] == '!':
    caps(name)
else:
    no_caps(name)