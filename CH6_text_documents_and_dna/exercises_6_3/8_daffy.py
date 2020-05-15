def daffy(word):
    string = ''
    for character in word:
        if character.lower() == 's':
            string += character + 'th'
        else:
            string += character
    return string

string = "That's despicable!"
print(daffy(string))
