# Build a program that displays when the user will retire and how many years she has to work till retirement.
import datetime

# get user age and age of retirement
age = int(input("What is your age? "))
r_age = int(input("At what age would you like to retire? "))

# calculate number of years they will have to work
yrs = r_age - age

date = int(datetime.date.today().strftime("%Y"))

print(f"It's {date}.  You will retire in {date + yrs}.")
print(f"You only have {yrs} years of work to go!")