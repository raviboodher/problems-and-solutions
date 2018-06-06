#!/usr/bin/python

def unique_char(s):
    """ (str) --> bool

    Determine if the string contains unique characters. If there are duplicate characters return False.

    Example: 'abcde' is True since it has all unique chars.
             'aabcde' is False since character 'a' appears two times in the string.

    >>> unique_char('abcde')
    True
    >>> unique_char('aabcde')
    False
    >>> unique_char('abCc')
    True
    """

    unique = set()

    for char in s:
        if char in unique:
            return False
        else:
            unique.add(char)
    return True
    
if __name__ == "__main__":
    import doctest
    print doctest.testmod(verbose=True)
