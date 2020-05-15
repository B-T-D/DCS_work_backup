def word_frequency(text):
    """Returns a dictionary containing the frequency of each word in the string
    text."""
    frequency = {}
##    text = text.strip('.')
    words = text.split()
    for word in words: # Smarter to use strip() on each word inside the loop rather than the full string
        word = word.strip('.!?,:;')
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency



string = "I am I."
print(word_frequency(string))
