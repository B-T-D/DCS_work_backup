def word_count_1(text):
    """Approximates the number of words in a string by counting the number of
    spaces, tabs, and newlines.

    Args:
        text (str): A string object.
        
    Returns:
        (int): Approx word count. Number of space, tab, or newline characters in
            text.
    """
    return text.count(' ') + text.count('\t') + text.count('\n')

def word_count_2(text):
    """Crudely corrects for double spaces."""
    return text.count(' ') - text.count('  ') + 1 # Add one for last word. 

def word_count_3(text):
    """Iterates over characters in string and increments a wordcount accumulator
    variable when character matches a whitespace."""
    count = 0
    for character in text:
        if character in ' \t\n': # Replaces the commented out if - or - or
##        if character == ' ' or character == '\t' or character == '\n':
            count = count + 1
    return count

def word_count_4(text):
    """ """
    count = 0
    prev_char = ' ' # Initialize it to a whitespace in case text starts with ws--don't want that to count as ending a word
    for character in text:
        if character in ' \t\n' and prev_char not in ' \t\n':
            count = count + 1
        prev_char = character
    return count

def word_count_5(text):
    """Final version--same as 4 but increments by 1 at the end if the text didn't
    end with a whitespace."""
    count = 0
    prev_char = ' ' # Initialize it to a whitespace in case text starts with ws--don't want that to count as ending a word
        # Init to empty string seemed to be fine both when text started with ws and didn't.
    for character in text:
        if character in ' \t\n' and prev_char not in ' \t\n':
            count = count + 1
        prev_char = character
    if prev_char not in ' \t\n':
        count = count + 1
    return count
    
def wc_file(file_name):
    """Return the number of words in the file with the given name.

    Args:
        file_name: the name of a text file

    Returns:
        (int): number of words in the file
    """
    text_file = open(file_name, 'r', encoding = 'utf-8')
    text = text_file.read()
    text_file.close()
    return word_count_5(text)


def main():
    short_text = ' This is not long.  But it will do. \n' + \
                 'All we need is a few sentences.'
    wc = word_count_1(short_text)
    print(wc)
    print(word_count_2(short_text))
##    for character in short_text:
##        print(character)
    print(word_count_3(short_text))
    print(f"wc4: {word_count_4(short_text)}")
    print(f"wc5: {word_count_5(short_text)}")

    print(wc_file('2701_0.txt'))

if __name__ == '__main__':
    main()
    
