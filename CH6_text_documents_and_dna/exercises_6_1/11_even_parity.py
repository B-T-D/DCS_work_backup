def even_parity(bits):
    """Return True if a string of mock-bits has even parity and False if not."""
    return bits.count('1') % 2 == 0

def even_parity_2(bits):
    """Same with DIY string.count()."""
    count = 0
    for character in bits:
        if character == '1':
            count += 1
    return count % 2 == 0

def make_even_parity(bits):
    new_bits = bits
    if even_parity_2(bits) == True:
        new_bits += '0'
    elif even_parity_2(bits) == False:
        new_bits += '1'
    return new_bits

print(even_parity('110101'))
print(even_parity('110001'))

print(even_parity_2('110101'))
print(even_parity_2('110001'))

print(make_even_parity('110101'))
print(make_even_parity('110001'))
