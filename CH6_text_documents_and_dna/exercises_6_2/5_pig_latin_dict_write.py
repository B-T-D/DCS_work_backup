

def pig_latin_dict(fname):
    """Prints the Pig Latin equivalent of every word in the dictionary .txt
    file fname, with exactly one word on each line of the file."""
    textfile = open(fname, 'r', encoding = 'utf-8')
    for line in textfile:
        print(pig_latin(line.rstrip()))
    textfile.close()

def pig_latin_dict_writer(filename, new_filename):
    textfile = open(filename, 'r', encoding = 'utf-8')
    new_textfile = open(new_filename, 'w', encoding = 'utf-8')
    for line in textfile:
        new_textfile.write(pig_latin(line.rstrip() + '\n'))
    textfile.close()
    new_textfile.close()

# Pig latin function from Codewars a while ago

def pig_latin(string):
    pstring = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    if pstring.startswith(tuple(vowels)):
        pstring += 'way'
    else:
        count = 0
        chars = list(pstring)
        while not chars[0] in vowels and count < len(pstring):
            chars.append(chars.pop(0))
            count += 1
        pstring = ''.join(chars) + 'ay'
    return pstring

def pig_latin_old(string):
    """Original CW function with the isalpha check."""
    pstring = ''
    if string.isalpha():
        pstring = string.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        if pstring.startswith(tuple(vowels)):
            pstring += 'way'
        else:
            count = 0
            chars = list(pstring)
            while not chars[0] in vowels and count < len(pstring):
                chars.append(chars.pop(0))
                count += 1
            pstring = ''.join(chars) + 'ay'
    return pstring
                              

fname = 'words.txt'
new_fname = 'piglatin_words.txt'
##pig_latin_dict(fname)
##print(pig_latin('string'))
##print(pig_latin('aesop'))
pig_latin_dict_writer(fname, new_fname)
