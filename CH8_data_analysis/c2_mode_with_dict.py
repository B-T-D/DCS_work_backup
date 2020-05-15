def mode(data):
    """Compute the mode of a non-empty list.

    Args:
        data (list): List of numbers.

    Returns:
        (list): The modes.
    """
    frequency = {}

    for item in data:
        if item in frequency: # item is alredy a key in frequency, i.e. already encountered that value once in iterating through the list
            frequency[item] += 1 # tally the item
        else:
            frequency[item] = 1 #Create a new entry kv pair {..., item: 1}

    frequency_values = list(frequency.values())
    max_frequency = max(frequency_values)

    # Build list of all items in data with frequency equal to max_frequency
    modes = []
    for key in frequency:
        if frequency[key] == max_frequency:
            modes.append(key)
    return modes

data = [18.9, 19.1, 18.9, 19.0, 19.3, 19.2, 19.3]
print(mode(data))
