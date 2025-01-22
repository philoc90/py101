# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

def crunch(string):
    new_string =""
    buffer = ""
    for char in string:
        if char != buffer:
            new_string += char
        buffer = char
    return new_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
# They do