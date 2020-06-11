from stack_additions import Stack

def palindrome(string):
    """Use the stack ADT to determine whether a string is a palindrome."""
    stringstack = Stack()
    for character in string:
        stringstack.push(character)

    reversed_string = ''
    while not stringstack.is_empty():
        character = stringstack.pop()
        reversed_string += character
    return string == reversed_string


string = 'string'
actual = palindrome(string)
expected = False
assert actual == expected, f"actual {actual}, expected {expected}"

string = 'a man a plan a canal panama'
string = ''.join(string.split(' '))
actual = palindrome(string)
expected = True
assert actual == expected, f"actual {actual}, expected {expected}"
