def count_names(words):
    count = 0
    for word in words:
        if word[0] == word[0].upper():
            count += 1
    return count

def count_names_chr_ord(words):
    count = 0
    for word in words:
        if 65 <= ord(word[0]) <= 90:
            count += 1
    return count

def sol_man(words):
    count = 0
    for word in words:
        if word[0] >= 'A' and word[0] <= 'Z':
            count += 1
    return count

test = ['Fili', 'Oin', 'Thorin', 'and', 'Bilbo', 'are', 'characters', 'in', 'a',
        'book', 'by', 'Tolkien']

assert count_names(test) == 5

assert count_names_chr_ord(test) == 5
