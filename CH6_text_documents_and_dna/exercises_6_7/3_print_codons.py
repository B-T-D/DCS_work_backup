def print_codons(dna):
    """Prints the codons (groups of 3 letters) starting at the left end in the
    string dna."""
    start = 0
    for i in range(start, len(dna), 3):
        codon = dna[start:start+3]
        if len(codon) == 3:
            print(codon)
        start += 3

def sol_man(dna):
    for index in range(0, len(dna) - 2, 3):
        print(dna[index:index+3])


print_codons('ggtacactgt')
('ggtacactgt')
