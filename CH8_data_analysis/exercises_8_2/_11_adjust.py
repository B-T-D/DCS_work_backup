def adjust(data):
    """Return an adjusted list without modifying the orifinal list. Don't
    use .copy() method, find a different way.

    Initial function p.365 was to subtract 0.01 from every float in a list
    of numbers.
    
    """
    new_data = []
    for d in data:
        new_data.append(d + 0.01)
    return new_data


data = [0.053, 0.071, 0.065, 0.074]

print(adjust(data))

assert data == [0.053, 0.071, 0.065, 0.074], "fail, orig data modified"
