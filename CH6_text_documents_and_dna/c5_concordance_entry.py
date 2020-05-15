def find(text, target):
    """Find the index of the first occurrence of the target in text.

    Args:
        text (str): A string object to search in
        target (str): String object to search for

    Returns:
        (int): Index of the first occurence of target in text, or -1 if not found
    """
    for index in range(len(text) - len(target) + 1): # iterate through and compare substrings of same length as target
        if text[index:index + len(target)] == target:
            return index
    return -1 # If not found
            

def concordance_entry(filename, word):
    """Print all lines in a file containing the given word.

    Args:
        filename (str): Name of the text file as a string
        word (str): The word to search for.

    Returns:
        None
    """

    text_file = open(filename, 'r', encoding = 'utf-8')
    line_count = 1
    for line in text_file:
        found = find(line, word)
        if found >= 0: # found the word in line
            space = ' ' * (80 - len(word) - found) # Print leading spaces to line up the target string in the output. Assuming 80 chars per line.
            print('{0:<6}'.format(line_count) + space + line.rstrip())
        line_count = line_count + 1
    text_file.close()


fname = '2701_0.txt' # moby dick

concordance_entry(fname, 'lashed')
