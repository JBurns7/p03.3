"""
Problem:

    The function 'add_and_sub' takes a list of integers.
    It should add up the items with an even index,
    and subtract the items with an odd index and print
    the total.

    e.g. add_and_sub([1, 2, 3, 4]) = 1 - 2 + 3 - 4 = -2


Tests:

    >>> add_and_sub([1, 2, 3, 4])
    -2
    >>> add_and_sub([5, 3, 2, 1, 4])
    7
    >>> add_and_sub([9, 10, 1, 6])
    -6
    >>> add_and_sub([5, 2, 3])
    6

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def add_and_sub(nums):

    total = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            total = total + nums[i]
        else:
            total = total - nums[i]
    print(total)
            

