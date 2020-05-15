def checksum(word):
    """Returns word with the appropriate checksum character added to the end.

    **Book uses a = 0, not a = 1.

    Args:
        word (str): string of all lowercase letters
    """

    sum = 0    
    for letter in word: # convert each letter to a number on zero-based index 0 to 25
        sum += ord(letter) - ord('a')
    return word + chr(ord('a') + sum % 26) # Convert sum to a letter and add it to word

def checksum_check(word):
    """Determines whether checksum character at the end of word is correct.

    Returns:
        (bool): True if checksum character is correct
        (bool): False if checksum character incorrect
    """
    text = word[:-1] # Split off the checksum character
    csc = word[-1]

    sum = 0 # Re-compute the correct checksum to expect
    for letter in text:
        sum += ord(letter) - ord('a')
    correct_csc = chr(ord('a') + sum % 26)
    return csc == correct_csc


"""Book just compresses a little bit by not using separate csc and text string
vars, instead just referring to the slices directly. Only actually need to
refer to each once, so no human-error-opportunity reduction from using a variable."""


letters = ['a', 'b', 'c', 'd', 'x', 'y', 'z']
words = ['snow', 'test', 'Geeter', 'Trouhnt', 'luRG', 'pingle']
##for word in words:
##    checksum(word)


print(checksum_check('snowp'))
print(checksum_check('snowy'))
