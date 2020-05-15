#!/usr/bin/env python3

from wordcount import count, getWordCounts

def test_count():
    quote = 'Diligence is the mother of good luck.'
    assert count(quote, 'the') == 2       # common cases
    assert count(quote, 'the ') == 1
    assert count(quote, 'them') == 0
    assert count(quote, ' ') == 6
    assert count(quote, '') == 0          # boundary cases
    assert count('a', '') == 0
    assert count('', '') == 0
    assert count('', quote) == 0
    assert count('', 'a') == 0
    assert count(quote, 'e') == 4
    assert count('e', 'e') == 1
    assert count('e', 'a') == 0
    assert count(quote, 'D') == 1
    assert count(quote, 'Di') == 1
    assert count(quote, 'Dx') == 0
    assert count(quote, '.') == 1
    assert count(quote, 'k.') == 1
    assert count(quote, '.x') == 0
    assert count(quote, quote) == 1       # corner cases
    assert count('the', quote) == 0
    
    print('Passed all tests of count!')
    
def test_getWordCounts():
    text = 'Call me Ishmael. Some years ago--never mind how long \
precisely--having little or no money in my purse, and nothing \
particular to interest me on shore, I thought I would sail about \
a little and see the watery part of the world.  It is a way I have \
of driving off the spleen and regulating the circulation.'
    
    assert getWordCounts(text, 'the', 20) == 4 / 15
    assert getWordCounts(text, 'spleen', 20) == 1 / 15
    
    print('Passed all tests of getWordCounts!')
        
def test():
    test_count()
    test_getWordCounts()

test()
