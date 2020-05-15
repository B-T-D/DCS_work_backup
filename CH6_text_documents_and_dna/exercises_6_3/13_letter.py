def letter(n):
    """Returns nth capital letter in the alphabet using chr() and ord()."""
    if (n < 1) or (n > 26):
        return None
    unicode_decimal = n + 64
    return chr(unicode_decimal)
    # Book uses ord('A') to get the starting point for the right span of unicode
    #   decimals, rather than just saying add 64:
    return chr(ord('A') + n - 1)

for i in range(27):
    print(f"for i = {i}:")
    print(letter(i))
    print('----')
