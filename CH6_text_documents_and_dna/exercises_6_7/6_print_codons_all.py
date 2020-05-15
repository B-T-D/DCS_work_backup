def print_codons_all(dna):
    """Prints the codons in all three reading frames by starting at offsets
    of 0, 1, and 2 from the left end."""

    for offset in [0, 1, 2]:
        for i in range(len(dna) - 2):
            print(dna[offset + i:offset + i + 3])
    
print_codons_all('ggtacactgtcat')
