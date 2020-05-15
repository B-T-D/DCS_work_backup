
def first_letter_words(words):
    """Returns a dict where key is the lowercase first letter and value is a
    list object listing all the words that start with that letter."""
    dict = {}
    for word in words:
        first = word[0].lower()
        if first in dict:
            dict[first].append(word)
        else:
            dict[first] = [word]
    return dict
        


words = "ant bee armadillo dog cat bombolecka".split()


print(first_letter_words(words))
