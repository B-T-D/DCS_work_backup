def get_inputs():
    """Prompt for the name of a text file, a word to analyze, and a window
    length. Read and return the test, word, and window length.

    Args:
        None

    Returns:
        (str): a text
        (str): word
        (int): window length
    """
    filename = input('Text file name: ') # get file name
    textfile = open(filename, 'r', encoding='utf-8') # read file
    text = textfile.read()
    textfile.close()

    word = input('Word: ') # get word
    window_length = int(input('Window length: ')) # get window length

    return text, word, window_length

def count(text, target):
    """Count the number of target strings in text.

    Precondition: Text and target are string objects.

    Postcondition: Returns number of occurrences of target in text.
    
    """
    assert isinstance(text, str) and isinstance(target, str), \
           'arguments must be strings'

    count= 0
    if target == '':
        return 0
    
    for index in range(len(text) - len(target) + 1):
        if text[index:index + len(target)] == target:
            count = count + 1
    return count

def get_word_counts(text, word, window_length):
    """Find the number of times word occurs in each window in the text.

    Args:
        text (str): A string containing a text
        word (str): A string
        window_length (int): The integer length of the window.

    Returns:
        (float): Average count per window
        (list): List of window counts

    Precondition: Text and word are string objects; text is larger than word;
        length of text is greater than window_length; and window_length is a positive integer.

    Postcondition: Returns a float giving the average count per
        window.
    
    """
    # Check that text and word are strings:
    assert isinstance(text, str) and isinstance(word, str), \
           'first two arguments must be strings'

    # Check that window_length is a positive integer:
    assert isinstance(window_length, int) and window_length > 0, \
           'window_length must be a positive integer'

    # Check that text is at least as long as window_length (to avoid dividing by zero):
    assert len(text) >= window_length, 'text must be longer than window_length'
    
    word_count = 0
    window_count = 0
    for index in range(0, len(text) - window_length + 1, window_length):
        window = text[index:index + window_length]
        window_count = window_count + 1
        words_in_window = count(window, word)
        word_count = word_count + words_in_window

    # double check against a division by zero error:
    assert window_count > 0, 'no windows were found'
    return word_count / window_count

def plot_word_counts(word_counts):
    """Plot a list of word frequencies.

    Args:
        word_counts (list): A list of word frequencies

    Returns:
        None
    """
    pass

def main():
##    test_text, test_word, test_length = get_inputs()
##    print(test_text, test_word, test_length)
    filename = '2701_0.txt'
    textfile = open(filename, 'r', encoding='utf-8')
    text = textfile.read()
    textfile.close()
    target = 'cunt'
    print(get_word_counts(text, target, 10))
    print(count(text, ''))
    print(len(text))
    

    # call get_inputs
    # call get_word_counts
    # call plot_word_counts
    # print average count per window

if __name__ == '__main__':
    main()
