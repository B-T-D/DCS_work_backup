def hamming(bits1, bits2):
    """Returns the Hamming distance between the two given bit strings. Strings
    are same length.

    Returns:
        (int): Number of index locations where the bits are different.
    """
    diffs = 0
    index = 0
    while index < min(len(bits1), len(bits2)):
        if bits1[index] != bits2[index]:
            diffs += 1
        index += 1
    # add in the difference between the longer and the shorter:
    diffs += max(len(bits1), len(bits2)) - min(len(bits1), len(bits2))
    return diffs

bits1 = '011100110001'
bits2 = '011000110101'
print(hamming(bits1, bits2))
print(hamming('000', '10011'))
