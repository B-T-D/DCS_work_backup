

def username(first, last):
    """Returns a person's username, specified as the last name followed by an
    underscore and the first initial."""
    return last + '_' + first[0]

print(username('martin', 'freeman'))
