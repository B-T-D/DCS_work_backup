
def find(text, target):
    """Find the index of the first whole-word occurrence of the target in text.

    Args:
        text (str): A string object to search in
        target (str): String object to search for

    Returns:
        (int): Index of the first occurence of target in text, or -1 if not found
    """
    for index in range(len(text) - len(target) + 1 + 1): # iterate through and compare substrings of same length as target
        if text[index:index + len(target) + 1] ==  ' ' + target or text[index:index + len(target)] == '\n' + target: # hasty slapped in additional +1 here and prev line
            return index
    return -1 # If not found

def sol_man(text, target):
    for index in range(len(text) - len(target) + 1):
        if (text[index:index + len(target)] == target) and \
           (index == 0 or text[index-1] in ' ') and \
           (index + len(target) == len(text) - 1 or text[index + len(target)] in ' .!?;-,\'"'):
            print(index)
            return index
        return -1

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
##        found = find(line, word)
        found = sol_man(line, word)
        if found >= 0: # found the word in line
            space = ' ' * (80 - len(word) - found) # Print leading spaces to line up the target string in the output. Assuming 80 chars per line.
            print('{0:<6}'.format(line_count) + space + line.rstrip())
        line_count = line_count + 1
    text_file.close()


fname = '2701_0.txt' # moby dick


print(sol_man('test string st', 'st'))
##concordance_entry(fname, 'lashed')
