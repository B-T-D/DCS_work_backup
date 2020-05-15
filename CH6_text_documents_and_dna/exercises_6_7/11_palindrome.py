def palindrome(dna):
    """Returns True if dna is the same as its reverse complement, False otherwise.
    (Reverse complement of 'gatc' would read from 3 'ctag' to 5, so reading
    both from 5 prime to 3 prime would be 'gatc')."""

    # get complement:
    rc = '' # prepend the complement of each character (to compile the reverse complement, appending would concatenate the complement)
    for char in dna:
        if char == 'a':
            rc = 't' + rc
        elif char == 't':
            rc = 'a' + rc
        elif char == 'c':
            rc = 'g' + rc
        elif char == 'g':
            rc = 'c' + rc
    return True if rc == dna else False    


dna = 'gaattc' # should return true
dna2 = 'gctgc' # should return false
print(palindrome(dna))
print(palindrome(dna2))
assert palindrome(dna)
assert palindrome(dna2)
