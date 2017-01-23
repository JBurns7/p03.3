"""
Problem:

    The function 'greater' takes a list of integers, nums, and another
    integer, n.  It should count the number of items in the list that
    are greater than n and print this.

Tests:

    >>> greater([1, 2, 3, 4], 2)
    2
    >>> greater([5, 3, 2, 7], 4)
    2
    >>> greater([3, 7, 4, 9, 10], 1)
    5
    >>> greater([1, 2, 3], 6)
    0

"""

# This code tests your solution. Don't edit it. 
import doctest 
def run_tests(): 
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE) 


def greater(nums, n):

    count = 0

    for i in nums:
        if i > n:
            count = count + 1

    print(count)
            

