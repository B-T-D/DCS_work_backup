
def no_vowels(text):
    string = ''
    for character in text:
        if not character.lower() in 'aeiou':
            string += character
    return string

print(no_vowels('no vowels'))
print(no_vowels('This is an example'))
