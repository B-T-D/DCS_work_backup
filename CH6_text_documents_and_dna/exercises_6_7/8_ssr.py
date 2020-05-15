def ssr(dna, repeat):
    """Returns the length (number of repeats) of the first SSR in dna that
    repeats the parameter repeat. If repeat is not found, return 0."""
    length = 0
    string = dna
    first_repeat = string.find(repeat)
    ssr_substring = string[first_repeat:]
    print(ssr_substring)
    for i in range(0, len(ssr_substring) - len(repeat)):
        slice = ssr_substring[i:i + len(repeat)]
        if slice == repeat:
            length += 1
    return length

def sol_man(dna, repeat):
    start = dna.find(repeat)
    if start < 0: # if repeat doesn't appear in dna at all
        return 0
    count = 0
    for index in range(start, len(dna), len(repeat)):
        if dna[index : index + len(repeat)] == repeat:
            count = count + 1
        else:
            return count
        
# Sol man also has an "Or" alternate solution using a while loop. 



print(ssr('atatatatatatatcgttcgatgccgtagtgactgcccgtatatatatatatgtg', 'at'))
print(sol_man('atatatatatatatcgttcgatgccgtagtgactgcccgtatatatatatatgtg', 'at'))
