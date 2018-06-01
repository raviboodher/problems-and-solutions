#!/usr/bin/python

import collections

def finder(list1, list2):
    """ (list, list) - > int

    we can sort both arrays and iterate through simultaneously.
    If you find difference in the values, stop it. This works if
    you dont want to deal with duplicates. Solution takes O(nlogn) time.

    >>> finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
    5
    >>> finder([1, 3, 5, 7], [2, 6, 8, 10])
    1
    """

    # using collections module to set default dictionary items to avoid key errors

    counts = collections.defaultdict(int)

    # Interate thought array and add a count for every instance.

    for num in list2:
        counts[num] += 1

    # interate through array2 and check item no in dictionary

    for num in list1:
        if counts[num] == 0:
            return num
        # subtract a count if available
        else:
            counts[num] -= 1

if __name__=='__main__':
    import doctest
    print doctest.testmod(verbose=True)



