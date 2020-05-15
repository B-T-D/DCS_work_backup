
def count(text, letter):
    """Returns number of occurrences of one character string letter in text,
    without using the builtin string.count() method."""
    text = text.lower()
    letter = letter.lower()
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count


count = count("Here's a string to count letters in", "t")
print(count)
