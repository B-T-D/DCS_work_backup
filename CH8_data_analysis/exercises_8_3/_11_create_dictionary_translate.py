def create_dictionary():
    """Creates a dictionary, inserts several english words as keys, and the Pig
    Latin or other language translations as values, and then returns the completed
    dictionary."""
    dict_german = {}
    words = ['book', 'mask', 'sword', 'notebook', 'computer',
             'mouse', 'monitor', 'headphones', 'hand', 'pen']
    translations = ['Buch', 'Maske', 'Schwert', 'die Kladde', 'Computer',
                    'die Maus', 'der Bildschirm', 'Kopfhörer', 'die Hand', 'Stift']
    i = 0
    assert len(words) == len(translations), f"Aborted, words and translations lists \
not same size"
    for i in range(len(words) - 1):
        dict_german[words[i]] = translations[i]
    return dict_german
                    
    

def translate():
    """Calls the create_dictionary() function to create a dictionary and
    then repeatedly asks for a word to translate. For each entered word, prints
    the translation using the dictionary. If word DNE in the dict, output should
    say so. Exit when string 'quit' is typed."""
    dict_german = create_dictionary()
    word = input('Enter a word to translate: ').lower()
    while word.lower() != 'quit':
        
        if word in dict_german.keys():
            print(dict_german[word])
        else:
            print(f"'{word}' isn't in the dict, try a different one")
        word = input('Enter a word to translate: ').lower()

def main():
    translate()

if __name__ == '__main__':
    main()
