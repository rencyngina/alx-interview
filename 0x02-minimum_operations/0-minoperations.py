#!/usr/bin/python3

"""It's a Minimum Operation project"""

def minOperations(n)

    """
    In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste.
    """
    
    if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            op += i
            i = 1
        i += 1
    return op
