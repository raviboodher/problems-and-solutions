#!/usr/bin/python
# -*- coding: utf-8 -*-


def pair_sum(my_list, k):
    """
    The O(N) algorithm uses the set data structure. We perform a linear pass from the beginning 
    and for each element we check whether k-element is in the set of seen numbers. 
    If it is, then we found a pair of sum k and add it to the output. If not, this element 
    doesn’t belong to a pair yet, and we add it to the set of seen elements. The complexity is O(N) 
    because we do a single linear scan of the array, and for each element we just check whether the 
    corresponding number to form a pair is in the set or add the current element to the set. Insert 
    and find operations of a set are both average O(1), so the algorithm is O(N) in total.

    >>> pair_sum([1, 3, 2, 2], 4)
    (1, 3)(2, 2)
    >>> pair_sum([3, 5, 8, 7, 1, -9], 8)
    (1, 7)(3, 5)
    >>> pair_sum([0, 12, 24, 36, -9], 36)
    (0, 36)(12, 24)
    >>> pair_sum([], 23)
    
    """

    if len(my_list) < 2:
        return

    # set for tracking elements seen so far
    seen = set()
    output = set()

    for num in my_list:
 
        target = k - num
  
        if target not in seen:
            seen.add(num)
        else:
            output.add( ((min(num, target)), max(num, target)) )

    print ''.join(map(str,list(output)))

#print pair_sum([1, 3, 2, 2], 4)
#print pair_sum([3, 5, 8, 7, 1, -9], 8)
#print pair_sum([0, 12, 24, 36, -9], 36)
#print pair_sum([], 36)


if __name__=='__main__':
    import doctest
    print doctest.testmod()
