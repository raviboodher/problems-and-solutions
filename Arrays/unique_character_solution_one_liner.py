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
    
    return len(set(s)) == len(s)
    
if __name__ == "__main__":
    import doctest
    print doctest.testmod(verbose=True)
