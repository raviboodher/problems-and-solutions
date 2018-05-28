
def anagram(s1, s2):
    """ (str, str) -> bool

    This program checks if the two strings are anagram

    >>> anagram("God", "doG")
    True
    >>> anagram('one', 'two')
    False
    >>> anagram('clint eastwood','old west action')
    True
    """

    s1 = s1.replace(' ', "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    import doctest
    print doctest.testmod()

