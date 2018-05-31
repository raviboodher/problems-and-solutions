#!/usr/bin/python


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

    # sort the lists using sort metthod
    list1.sort()
    list2.sort()

    # Compare elements in the sorted lists
    for num1, num2 in zip(list1, list2):
        if num1 != num2:
            return num1

    return list1[-1]


if __name__=='__main__':
    import doctest
    print doctest.testmod(verbose=True)
