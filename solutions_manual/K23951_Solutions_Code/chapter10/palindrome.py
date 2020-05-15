#!/usr/bin/env python3

def palindrome(s):
    """Determine whether a string is a palindrome.

    Parameter: a string s

    Return value: a Boolean value indicating whether s is a palindrome
    """

    if len(s) <= 1:    # base case
        return True
    return s[0] == s[-1] and palindrome(s[1:-1])
