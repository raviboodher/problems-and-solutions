

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


if __name__=='__main__':
    import doctest
    print doctest.testmod()
