def print_frequencies(frequency):
    """Prints a formatted table of frequencies stored in dict frequency. With
    key values in the table in sorted order.

    Returns:
        None
    """
    keys_list = list(frequency.keys())
    keys_list.sort()
    print(f"Key        Frequency")
    for k in keys_list:
        print(f"{k}        {frequency[k]}")


def get_frequency(data):
    frequency = {}

    for item in data:
        if item in frequency: # item is alredy a key in frequency, i.e. already encountered that value once in iterating through the list
            frequency[item] += 1 # tally the item
        else:
            frequency[item] = 1
    return frequency

data = [18.9, 19.1, 18.9, 19.0, 19.3, 19.2, 19.3]
frequency = get_frequency(data)
print_frequencies(frequency)
    
