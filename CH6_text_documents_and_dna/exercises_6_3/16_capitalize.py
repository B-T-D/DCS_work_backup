
def capitalize(word):
    """Returns version of the string word with first letter capitalized."""
    string = word[0].upper()
    for character in word[1:]:
        string += character
    return string

def sol_man(word):
    """Book does it using chr() and ord()"""
    if word[0] >= 'A' and word[0] <= 'Z':
        return word # If the word was already capitalized just return it as-is
    return chr(ord(word[0]) - ord('a') + ord('A')) + word[1:]

words = ['test', 'Geeter', 'Trouhnt', 'luRG', 'pingle']
for word in words:
    print(capitalize(word))

print("book's")
for word in words:
    print(sol_man(word))
