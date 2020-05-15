
def strip(filename, new_filename):
    """Creates a new version of the file with the given filename in which all
    whitespace characters have been removed, and saves into new_filename."""
    textfile = open(filename, 'r', encoding = 'utf-8')
    new_textfile = open(new_filename, 'w') # Apparently don't need to specify encoding here (or at least book doesn't)
    for line in textfile:
        new_line = line.replace(' ', '')
        new_line = new_line.replace('\t', '')
        new_line = new_line.replace('\n', '')
        new_textfile.write(new_line)
    textfile.close()
    new_textfile.close()

fname = 'words.txt'
new_fname = 'ws_stripped_words.txt'
strip(fname, new_fname)
