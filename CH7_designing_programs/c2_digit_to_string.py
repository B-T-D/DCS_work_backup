"""Originally from 6.3"""

def int_to_string(value):
    """Convert an integer into its corresponding string representation.

    Args:
        value (int): Integer with any number of digits

    Returns:
        (str): String object representing each digit in value.
    """
    int_string = ''
    while value > 0:
        digit = value % 10
        value = value // 10
        int_string = digit_to_string(digit) + int_string # prepend it
    return int_string

def digit_to_string(digit):
    """Converts an integer digit to its corresponding string representation.

    Precondition: Digit is an integer between 0 and 9

    Postcondition: returns the string representation of digit, or None if digit
        is not an integer between 0 and 9.
    """
 #   if not isinstance(digit, int) or (digit < 0) or (digit > 9):
#        return None
    assert isinstance(digit, int), 'Digit must be an integer'
    assert (digit >= 0) and (digit <= 9), 'Digit must be in [0..9]'
    return chr(ord('0') + digit)


tests = [1, 2, 3, 456, '9', 'nine', 'quux', 123.4]

for t in tests:
    print(digit_to_string(t))

tests = [123, 233, 989, 'one hundred', '998', 123.4]
for t in tests:
    print(int_to_string(t))
