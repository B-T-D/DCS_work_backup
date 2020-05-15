
def encipher(text, shift):
    """
    Args:
        text (str): String of all upper case characters.
        shift (int): Fixed number of alphabet-order positions to shift each letter.
    """

    enciphered = ''
    # For each letter...
    for letter in text:
        if letter >= 'A' and letter <= 'Z': # Set non-alpha chars aside
            # Convert it to a number:
            x = ord(letter) - ord('A')
            x = x + shift # add shift to that number
            x = x % 26 # modulo 26 to wrap around
            x = chr(ord('A') + x) # Back to letter
        else:
            x = letter
        enciphered += x
    return enciphered

# book's way handles the space issue by just leaving a space a space:
def sol_man(text, shift):
    pass
    # Integrated above--the if else

print(encipher('ABC XYZ TEST', 3))
# TODO space character apparently collides with 'T'--both encipher to 'W'

        
        
    
