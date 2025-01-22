# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

# get input as float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#print the math
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)