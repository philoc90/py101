# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).
def multiply(num1, num2):
    return num1 * num2

def square(num):
    return num * num

# I did not understand the instructions, oops.  Let's see what we can do for the further exploration, now that I understand.

def exponent(base, power):
    counter = 1
    product = base
    while counter < power:
        product = multiply(product, base)
        counter += 1
    return product