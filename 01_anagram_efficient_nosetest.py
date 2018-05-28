def anagram(s1, s2):

    """ (str, str) -> bool

    This program checks if the strings are anagram or not.

    >>> anagram('Dog', 'God')
    True
    >>> anagram('My India', 'One India')
    False
    >>> anagram('clint eastwood','old west action')
    True

    """

    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Edge case check
    if len(s1) != len(s2):
        return False

    count = dict()
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print('ALL TEST CASES PASSED')


# Run Tests
t = AnagramTest()
t.test(anagram)
   
