def cpg(dna):
    """Returns the fraction of dinucleotides that are cg."""
    count = 0
    for index in range(0, len(dna)):
        if dna[index:index + 2] == 'cg':
            count += 1
    return count / (len(dna) / 2)



print(cpg('atcgttcg'))
