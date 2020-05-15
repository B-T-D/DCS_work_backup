def sentences(text):
    """Returns the number of sentences in the string text."""
    count = 0
    prev_char = '' # empty string
    for character in text:
        if character in '.?!' and prev_char not in '.?!':
            count += 1
        prev_char = character
    if prev_char not in '.?!':
        count += 1 # This will count a string-ending sentence with no punctuation mark as an additional sentence.
    return count


text = "This is a test string. It will have sentences for the function to count." + \
    " It has three sentences."

print(text)
print(sentences(text))

text = "This is a test string?????!!!! It will have sentences for the function to count." + \
    "  It has four sentences. Here's the fourth?!?????..???"
print(text)
print(sentences(text))

text = "Does it count a sentence that ends the string but has no end punctuation?" + \
       " If yes then this string should return 2"
print(text)
print(sentences(text))

    
