def value(digit):
    """Returns the integer value corresponding to the parameter string digit.
    e.g. value('5') should return integer 5."""

    if (digit < '0') or (digit > '9'):
        return None
    return ord(digit) - ord('0')

str_digits = [str(i) for i in range(10)]
print(str_digits)

for d in str_digits:
    obj = value(d)
    print(f"object is {obj} and it's a {type(obj)}")

    
