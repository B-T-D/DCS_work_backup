
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
    text_file = open(filename, 'r', encoding = 'utf-8')
    line_count = 1
    for line in text_file:
        found = find(line, word)
        if found >= 0: # found the word in line
            space = ' ' * (80 - len(word) - found) # Print leading spaces to line up the target string in the output. Assuming 80 chars per line.
            print('{0:<6}'.format(line_count) + space + line.rstrip())
        line_count = line_count + 1
    text_file.close()
        
    

def concordance(dict_fname, text_fname):
    """Uses dictionary (i.e. list of words and definitions) with given file name
    and the concordance_entry function to print a complete concordance for the
    text with the given filename.

    A highly inefficient way to compile a concordance.
    """

    dict_file = open(dict_fname, 'r', encoding = 'utf-8')
    for line in dict_file:
        print(f"word is {line.rstrip()}")
        concordance_entry(text_fname, line.rstrip())
        print()
    dict_file.close()




dict_fname = r"C:\Users\Ben\Desktop\Python_DCS_book\CH6_text_documents_and_dna\exercises_6_2\words.txt"
text_fname = "2701_0.txt"
concordance(dict_fname, text_fname)

