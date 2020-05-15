import random

def percentile(data, value):
    """Returns the percentile of value in the list named data."""
    count = -1 # Counter of data elements less than or equal to value. -1 to
    #   not count the value itself while also allowing for other values equal to it.
    for d in data:
        if d <= value:
            count += 1
    return count / len(data) * 100
    


data = [(i * random.random()) for i in range(0, 999)]
##for d in data:
##    print("\t" + str(d))
data.append(1000)
print(len(data))

print(percentile(data, 1000))

assert percentile(data, 1000) == (999 / 1000) * 100, \
       f"fail, returned {percentile(data, 1000)}"
