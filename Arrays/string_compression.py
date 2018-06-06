#!/usr/bin/python

def compress(s):
    """ (str) -> (str)
    Example Question - https://www.geeksforgeeks.org/run-length-encoding/

    We use RunLenght Compression algorithm to solve the problem.
  
    Solution has O(n) order.

    >>> compress("AAAABBC")
    'A4B2C1'
    >>> compress("aAbBcc")
    'a1A1b1B1c2'
    
    """

    # Create an empty string
    
    result = ""
    length = len(s)

    # Check for length 0
    if length == 0:
        return 0

    # Check for length 1
    if length == 1:
        return s + "1"

    # initialize the values
    last = s[0]
    count = 1
    i = 1

    while i < length:
        
        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            count += 1
        else:
            # Otherwise store the previous data
            result = result + s[i - 1] + str(count)
            count = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    result = result + s[i - 1] + str(count)

    return result
     


if __name__ == "__main__":
    import doctest
    print doctest.testmod(verbose=True)
