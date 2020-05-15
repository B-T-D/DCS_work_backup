
def int_to_str(n):
    """Converts a positive integer value n to its string equivalent without
    using builtin str()."""

    
    # Make list of the digits
    digits = []
    digit = 0
    i = 1
    while n > 0:
        digit = n % 10
        digits.insert(0, int(digit))
        n = (n - digit) / 10
        i += 1

    string = ''
    for digit in digits:
        string += chr(ord('0') + digit)
    return string

def sol_man(n):
    int_string = ''
    while n > 0:
        digit = n % 10
        n = n // 10
        int_string = digit_to_string(digit) + int_string # NB to add to the front
    return int_string

def digit_to_string(digit):
    """Function from the chapter body that the book's solution calls."""
    if (digit < 0) or (digit > 9):
        return None
    return chr(ord('0') + digit)

n = 98765
object = int_to_str(n)
print(object)
print(type(object))
print(f"book's: {sol_man(n)}")
