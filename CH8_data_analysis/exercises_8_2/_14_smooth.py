def smooth(data, window_length):
    """Returns a new list that containst the values in data, averaged over
    a window of the given length."""
    smoothed = []
    for i in range(0, len(data)):
        window_start = i - window_length // 2
        window_end = (i + window_length // 2) + 1
        data_slice = data[window_start:window_end]
        value = sum(data_slice) / window_length
        smoothed.append(value)
    return smoothed

def sol_man(data, window_length):
    # Seems to me like a really odd and counterintuitive way to do this...
    smoothed = []
    sum = 0
    for value in data[:window_length]: # All he's doing here is getting the
                # denominator for the mean. Instead of using builtin sum(). 
        sum += value
    smoothed.append(sum / window_length)

    for index in range(1, len(data) - window_length + 1):
        sum -= data[index - 1]
        sum += data[index + window_length - 1]
        smoothed.append(sum / window_length)
    return smoothed

data = [i for i in range(1, 11)]
print(data)
data_2 = smooth(data, 2)
print(data_2)

data_sm = data
data_sm2 = smooth(data, 2)
print(data_sm2)

