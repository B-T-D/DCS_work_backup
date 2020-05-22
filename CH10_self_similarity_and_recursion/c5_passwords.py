def passwords(length, characters):
    """Return a list of all possible passwords with the given length, using
    the given characters.

    Args:
        length (int): the length of the passwords
        characters (str): a string containing the possible characters

    Returns:
        (list): a list of all possible passwords with the given length, using
        the given characters
    """
    if length == 0:
        return ['']

    shorter = passwords(length - 1, characters)

    password_list = []
    for character in characters:
        for shorter_password in shorter:
            password_list.append(character + shorter_password)

    return password_list


length = 5
characters = 'abcde'

password_list = passwords(length, characters)

assert len(password_list) == 5 ** 5, "total passwords should equal number \
of characters raised to power of number of characters in tha password, i.e. \
len(characters) ** length"

