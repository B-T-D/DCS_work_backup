def vowels(word):
    """Uses count method to return the number of vowels in the string word.
    Returns:
        (int): The vowel count
    """
    word = word.lower()
    vowels = 0
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        vowels +=  word.count(vowel)
    return vowels

print(vowels('aeiou test method'))
