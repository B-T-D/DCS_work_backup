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

letters = ['a', 'b', 'c', 'd', 'x', 'y', 'z']
words = ['snow', 'test', 'Geeter', 'Trouhnt', 'luRG', 'pingle']
##for word in words:
##    checksum(word)

print(checksum('snow'))
