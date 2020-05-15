
def first_letter_count(words):
    """Returns dict with lower case letters as keys and the number of words in
    (list) words that begin with that letter."""
    dict = {}
    for word in words:
        flet = word[0].lower()
        if flet in dict:
            dict[flet] += 1
        else:
            dict[flet] = 1
    return dict
    

words = "ant bee armadillo dog cat".split()
correct_dict = {'a': 2, 'b': 1, 'c': 1, 'd': 1}

assert first_letter_count(words) == correct_dict, f"fail {first_letter_count(words)}"
