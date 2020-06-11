import stack

def convert(number, base):
    """Use the stack ADT to convert a non-negative base-10 integer value in
    any base. (but return that as a string not an int--because if base > 10,
    need to use letters, like how hex uses 0-9 and then needs A-F as well.)

    Args:
        number (int): a non-negative integer
        base (int): the base in which to represent the value

    Returns:
        (str): a string of the digits.
    """

    digit_stack = stack.Stack()
    while number > 0:
        digit = number % base
        digit_stack.push(digit)
        number = number // base

    number_string = ''
    while not digit_stack.is_empty():
        digit = digit_stack.pop()
        if digit < 10:
            number_string = number_string + str(digit)
        else:
            number_string = number_string + chr(ord('A') + digit - 10)
    return number_string

print(convert(234, 16))
print(convert(234, 17))



