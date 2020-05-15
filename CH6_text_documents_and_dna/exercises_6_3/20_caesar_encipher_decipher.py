
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
            x = letter # non alpha chars aren't modified. E.g. space stays a space.
        enciphered += x
    return enciphered

def cipher(text, shift, decrypt=False):
    """
    Args:
        text (str): String of all upper case characters.
        shift (int): Fixed number of alphabet-order positions to shift each letter.
        decrypt (bool): If True, return the decipher of text

    * Book does it by flippiing shift to -(shift). 
    """

    message = ''
    for letter in text:
        if letter >= 'A' and letter <= 'Z': # Set non-alpha chars aside
            # Convert it to a number:
            x = ord(letter) - ord('A')
            if decrypt == True:
                x = x - shift # Shift other direction to decrypt
            else:
                x = x + shift
            x = x % 26 # modulo 26 to wrap around
            x = chr(ord('A') + x) # Back to letter
        else:
            x = letter # non alpha chars aren't modified. E.g. space stays a space.
        message += x
    return message

    

print(cipher('IDES OF MARCH', 3))
print(cipher('LGHV RI PDUFK', 3, True))
# TODO space character apparently collides with 'T'--both encipher to 'W'

        
        
    
