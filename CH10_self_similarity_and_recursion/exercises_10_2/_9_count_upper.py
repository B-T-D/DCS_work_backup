def count_upper(s):
    """Returns the number of uppercase letters in (str) s, recursively."""
    count = 0
    if ord('A') <= ord(s[0]) <= ord('Z'):
        count = 1
    else:
        count = 0
    if len(s) == 1:
        if ord('A') <= ord(s) <= ord('Z'): # i.e. between 65 and 90
            return 1
        else:
            return 0
    return count + count_upper(s[1:])

def solman(s):
    if s == '':
        return 0
    if s[0].isupper():
        return 1 + solman(s[1:])
    return count_upper(s[1:])

s = 'StrIng'
control = 2
returned = count_upper(s)

assert returned == control, f"{returned} != {control}"

print(count_upper('SSSSSSS'))
print(count_upper('lowercase'))
print(count_upper('Type here to Search'))

print('----')
print(solman('SSSSSSS'))
print(solman('lowercase'))
print(solman('Type here to Search'))
