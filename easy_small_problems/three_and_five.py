# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

def multisum(num):
    # initialize return value
    sum = 0
    # make sure i is an int
    for i in range(1, num + 1):
        # check to see if either condition is true
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
