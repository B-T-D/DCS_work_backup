# code along only

from matplotlib import pyplot

def histogram(data):
    """Displays a histogram of the values in the list data using the bar function
    from matplotlib."""

    frequency = {}

    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    indices = range(len(frequency))
    pyplot.bar(indices, frequency.values(), align = 'center')
    pyplot.xticks(indices, list(frequency.keys()))
    pyplot.xlabel('Data')
    pyplot.ylabel('Frequency')
    pyplot.show()
        


data = [18.9, 19.1, 18.9, 19.0, 19.3, 19.2, 19.3]
histogram(data)
