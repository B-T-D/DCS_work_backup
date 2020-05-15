def find_codon(dna, codon):
    """Returns the index of the first occurrence of the given codon in the
    string dna.
    """
    for index in range(0, len(dna) - 2): # Leave step at the default 1
        slice = dna[index:index+3]
        if slice == codon:
            return index
    return -1 # Return -1 if not found



print(find_codon('acgatgtcgatctttatggtatgcttcc', 'cga'))
