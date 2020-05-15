"""Doing to the book's simpler spec, i.e. no '-way' ending for words
that start with vowel, just slap 'ay' on the end of everything."""

def piglatin(word):
    return word[1:] + word[0] + 'ay'

print(piglatin('python'))
