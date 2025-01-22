# Write a function that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the argument is a negative number, return it as-is.

def negative(num):
    #check if input is larger than zero
    if num > 0:
        # if so, make it negative
        return num * -1
    else:
        # if not, do nothing
        return num
    
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True

# alternatively we could use the abs function hehe oops~