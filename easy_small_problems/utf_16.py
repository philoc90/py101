# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

def utf16_value(string):
    string_value = 0
    for char in string:
        string_value += ord(char)
    return string_value