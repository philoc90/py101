# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# define function
def short_long_short(first, second):
    # check which is longer
    if len(first) > len(second):
        # return the shorter, then longer, then shorter
        return second + first + second
    else:
        return first + second + first
