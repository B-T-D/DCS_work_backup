
def longest_ssr(dna):
    """
    Returns:
        most_repeated (str): The two-character substring ('dinucleotide') that is
        repeated the most times. If more than one pairs tie for most repetitions,
        returns first one to be repeated that many times.
    """
    max_repeats = 0
    most_repeated = ''
    for i in range(0, len(dna) - 1):
        d = dna[i:i+2]
        j = 2
        repeats = 0
        while dna[i+j:i+j+2] == d and j <= len(dna):
            repeats += 1
            j += 2
        if repeats > max_repeats:
            max_repeats = repeats
            most_repeated = d
    return most_repeated

def sol_man(dna):
    longest = 0
    for b in 'cgat': # iterates over all possible letters in dna string
        for c in 'cgat':
            repeat = b + c
##            count = ssr2(dna, repeat)
##      Relies on calling prev exercise function. 
    









dna = 'atatatatatatatcgttcgatgccgtagtgactgcccgtatatatatatatgtg'
dna2 = 'atatatagcgcgcgcgcgcgcgcgcgcgcgcgcgcgcgcgcgcgcgcgctatatatcgttcgatgccgtagtgactgcccgtatatatatatatgtg'

print(longest_ssr(dna))
print(longest_ssr(dna2))
