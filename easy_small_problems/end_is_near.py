# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.

def penultimate(string):
    #split on spaces only
    words = string.split(" ")
    #return 2nd to last item
    return words[-2]


# Further Exploration

# Our solution ignored two edge cases since we explicitly stated that you didn't have to handle them: strings that contain no words or just one word.

# Suppose we need a function that retrieves the middle word of a phrase/sentence. What edge cases need to be considered? How would you handle those edge cases without ignoring them? Write a function that returns the middle word of a phrase or sentence. It should handle all of the edge cases you thought of.

#if they give no input default to empty string
def middle(string=""):
    #split again
    print(string)
    string = string.strip()
    print(string)
    words = string.split()
    print(words)
    #if even, get the mid-point
    if len(words) % 2 == 0:
        return words[int(len(words) / 2)]
    #if odd, get the same midpoint as an even.  Ex: the midpoint for 5 and 6 are both 3, the midpoint for 7 and 8 are both 4, etc
    else:
        return words[int((len(words) - 1) / 2)]
    
print(middle(" last word test ") == "word")