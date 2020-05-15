def count_vowels(word):
    word = word.lower()
    count = 0
    for character in word:
##        if character in ['a', 'e', 'i', 'o', 'u']:
            # can just do if character in 'aeiou', don't need a list.
        if character in 'aeiou':
            count += 1
    return count

def count_vowels_swapped_loops(text):
    """How much slower does it run if the loop that iterates over each
    character in the string is inside the loop that iterates over the vowels?
    I.e. if you cycle through every word in the string for each vowel instead
    of every vowel for each character?

    ... constant 5 vowels...for string of n characters:
        looping each vowel for each character should be 5n comparisons.
        And 5n + n "times" through a for loop. Right?

    ...Would looping each character for each value be...
        5 vowels * n characters...so still 5n?
    You're comparing each character against each vowel either way, right?
    """
    pass


word = 'test with more vowels'
print(count_vowels(word))
    
