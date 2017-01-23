"""
Problem:

    The function 'cons' takes a list of integers, nums.
    If any two consecutive items in the list are the same, it
    should print "Match", otherwise it should print "No match"

Tests:

    >>> cons([1, 1])
    Match
    >>> cons([1, 2, 3, 4, 4, 5])
    Match
    >>> cons([3, 4, 3, 4, 3])
    No match
    >>> cons([])
    No match

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def cons(nums):

    match = 0

    

    for i in range(len(nums) -1):
        if nums[i] == nums[i+1]:
            match = match + 1

    if match > 0:
        print("Match")

    else:
        print("No match")
            


