
# http://discovercs.denison.edu/chapter8/scrabble.txt

import urllib.request as web

def first_letter_count(filename):
    """Returns dict with lower case letters as keys and the number of words in
    (list) words that begin with that letter.

    Args:
        file (file object): filename of A txt file object returned by .open() or urllib

    Returns:
        (dict): Lower case letters as keys, number of words in file that start
            with that letter as value.
    """

    file = open(filename, mode='r', encoding = 'utf-8')
    dict = {}

    for line in file:
        words = line.split()
        for word in words:
            first = word[0].lower()
            if first in dict:
                dict[first] += 1
            else:
                dict[first] = 1
    file.close()
    return dict

def sol_man(filename):
    text = open(filename, 'r', encoding = 'utf-8')
    words = text.read() # reads into one giant string
    text.close()
    words = words.split()
    dictionary = {}
    for word in words:
        word = word.strip('.!?,:;')
        first = word[0].lower()
        if first in dictionary:
            dictionary[first] += 1
        else:
            dictionary[first] = 1
    return dictionary

url = 'http://discovercs.denison.edu/chapter8/scrabble.txt'
filename = 'scrabble.txt'
file = web.urlopen(url)
dict = first_letter_count(filename)
print(dict)
print('----')
dict = sol_man(filename)
print(dict)
