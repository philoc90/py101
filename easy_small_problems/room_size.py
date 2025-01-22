#Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

length = float(input("What is the length of the room in meters? "))
width = float(input("What is the width of the room in meters? "))

area_in_meters = length * width
area_in_feet = area_in_meters * 10.7639

print(f"The area of your room is {area_in_meters} square meters, or alternatively {area_in_feet} square feet.")