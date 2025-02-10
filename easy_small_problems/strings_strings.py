# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(number):
    number_sequence = []
    for i in range(number):
        if i % 2 == 0:
            number_sequence.append("1")
        else:
            number_sequence.append("0")
    return (''.join(number_sequence))

print(stringy(6))
print(stringy(9))
print(stringy(4))
print(stringy(7))
