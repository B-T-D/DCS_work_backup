# solman is better, mine lazily / hurriedly just mutates/overwrites. 


def pmf(frequency):
    """Returns a dictionary containing the probability mass function of the
    frequency dictionary. I.e. Each frequency value divided by the total number
    of items in the data set."""
    pmf = {}
    freq_values = list(frequency.values())
    sum_freqs = sum(freq_values)
    for key, value in frequency.items():
        frequency[key] = value / sum_freqs
    return frequency

def sol_man(frequency):
    total = 0
    for key in frequency:
        total = total + frequency[key]
    pmf_dict = {}
    for key in frequency:
        pmf_dict[key] = frequency[key] / total
    return pmf_dict

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
print(frequency)
print(sol_man(frequency))
print('---')
print(pmf(frequency))
