def find_atg(dna):
    """Returns a list of indices of all positions of the codon ATG in the given
    dna string."""
    dna = dna.lower()
    indices = []
    for index in range(len(dna)):
        if dna[index:index + 3] == 'atg':
            indices.append(index)
    return indices if indices != [] else -1
    
    

print(find_atg('acgatgtcgatctttatggtatgcttcc'))

    
