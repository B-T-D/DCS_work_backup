def reverse(text):
    """Returns a copy of the string text in reverse order."""
    string = ''
    for i in range(len(text)):
        string += text[-i - 1]
    return string

# *** Can simply add it to the front of the string--much cleaner:

def sol_man(text):
    string = ''
    for character in text:
        string = character + string # Add the character to the start of the string
    return string

print(reverse('test'))
print(sol_man('test'))
