
def no_spaces(sentence):
    """Returns the string 'sentence' with spaces replaced with underscores,
    without using builtin string.replace()."""
    new_string = ''
    for character in sentence:
        if character == ' ':
            new_string += '_'
        else:
            new_string += character
    return new_string

string = "Here's a string to test."
string = no_spaces(string)
print(string)
