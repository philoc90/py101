# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.
# For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

# To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.
# note: this is arbitrary, not mathematical.  1700, 1800, and 1900 are not leap years simply by choice.  They would be otherwise.
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
