# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

def repeat(word, num):
    #basic while loop
    counter = 0
    while counter < num:
        print(word)
        counter += 1


repeat('Hello', 3)