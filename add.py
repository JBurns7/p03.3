"""
Problem:

    The function 'add' takes a list of integers, nums.
    It should add them all up and print the total.

Tests:

    >>> add([1, 2, 3])
    6
    >>> add([5, 7, 9])
    21
    >>> add([2, 3, -6])
    -1

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 



def add(nums):

    total = 0

    for n in nums:
        total = total + n
    print(total)
