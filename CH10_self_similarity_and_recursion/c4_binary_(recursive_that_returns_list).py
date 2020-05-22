def binary(length):
    """Return a list of all binary strings with the given length.

    Args:
        length (int): the length of the binary strings

    Returns:
        (list): a list of all binary strings with the given length
    """

    if length == 0: # base case
        return['']

    shorter = binary(length - 1) # recursively get shorter strings

    bit_strings = [] # create a list of "bit strings" (binary strings)
                    # with prefix 0
    for character in ['0', '1']:
        for short_string in shorter:
            bit_strings.append(character + short_string)

    return bit_strings # return all bit strings

length = 3
print(binary(length))
