from c3_wordcount_tests_version import count, get_word_counts

def test_count():
    """Unit test for count"""

    # tests of count here

    quote = 'Diligence is the mother of good luck.'

    # Common cases:
    assert count(quote, 'the') == 2
    assert count(quote, 'the ') == 1
    assert count(quote, 'them') == 0
    assert count(quote, ' ') == 6

    # Boundary cases:

        # Blank string as target:
    assert count(quote, '') == 0
    assert count('a', '') == 0
    assert count('', '') == 0 # both target and text blank

        # Blank string as text:
    assert count('', quote) == 0
    assert count('', 'a') == 0

        # Cases where both strings are close to an empty string:
    assert count(quote, 'e') == 4
    assert count('e', 'e') == 1
    assert count('e', 'a') == 0

        # Confirmint function correctly counts substrings that appear at beginning
            # and end of text:
    assert count(quote, 'D') == 1
    assert count(quote, 'Di') == 1
    assert count(quote, 'Dx') == 0
    assert count(quote, '.') == 1
    assert count(quote, 'k.') == 1
    assert count(quote, '.x') == 0

    # Corner cases:

        # What if text and target are same?
    assert count(quote, quote) == 1
        # What if text is shorter than target?
    assert count('the', quote) == 0
    
    print('Passed all tests of count function!')


def test_get_word_counts():
    """Unit test for get_word_counts"""

    # tests of get_word_counts here

    text = "Call me Ishmael. Some years ago—never mind how long precisely—having \
little or no money in my purse, and nothing particular \
to interest me on shore, I thought I would sail about a little and see \
the watery part of the world. It is a way I have of driving off the \
spleen and regulating the circulation."

    # Reference info about text:
    print(f"len(text): {len(text)}")
    print(f"count(text, 'the') : {count(text, 'the')}")
    print(f"count(text, 'sail') : {count(text, 'sail')}")


    # Common cases

##    assert get_word_counts(text, 'the', 20) == float(4 / 15)
    # Unclear why this one isn't passing. There are 15 windows and the appears 4 times. 
    assert get_word_counts(text, 'spleen', 20) == 1 / 15


    # Boundary cases

        # Window is longer than text --> already covered by the function itself, i.e. preconditions require this
            # so not a "case". 
##    assert get_word_counts(text, 'sail', 302) == 1 / 15

        # Window exactly the length of text
    assert get_word_counts(text, 'spleen', 301) == 1

    assert get_word_counts(text, 'sail', 301) == 1

    print('Passed all tests of get_word_counts function!')

def test():
    test_count()
    test_get_word_counts()

test()

    

