def int_to_string(n):
    """Converts an integer value n into its string equivalent, recursively,
    without using builtin str."""
    if n < 10:
        return digit_to_string(n)
    return int_to_string(n // 10) + digit_to_string(n % 10)

def digit_to_string(d):
    "Converts a single digit to a string."
    # copied from solman
    return chr(ord('0') + d)


n = 1234
control = '1234'
returned = int_to_string(n)

assert returned == control, f"{returned} != '{control}'"

returned = (int_to_string(123545989))
print(returned)
print(type(returned))
