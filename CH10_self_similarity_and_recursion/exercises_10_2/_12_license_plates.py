def license_plates(length, letters, numbers):
    """Returns a list of strings representing all possible license plates of
    the form 'ABC 123' (for length=3).

    Args:
        length (int): number of characters in each of letters and numbers
        letters (str): string containing all the possible letters that can
            be used on the plates
        numbers (str): string containing all digit characters that can be
            used on the plates
    """
##    assert length == len(letters) == len(numbers), f"{length} != {len(letters)} != {len(numbers)}"

    if length == 0:
        return [' ']

    shorter = license_plates(length - 1, letters, numbers)

    plates_list = []
    for letter in letters:
        for number in numbers:
            for plate in shorter:
                plates_list.append(letter + plate + number)
    
    return plates_list
    


returned = license_plates(2, 'XY', '12')
print(returned)
assert len(returned) == 16
