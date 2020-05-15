from sixteen_search import search


def intersect(data1, data2):
    """Returns True if the two lists have any common elements, else False."""
    for d in data1:
        if search(data2, d) == True:
            return True
    return False



data1 = ['Katniss', 'Peeta', 'Gale']
data2 = ['Foxface, Marvel', 'Glimmer']
assert intersect(data1, data2) == False
data2 = ['Gale', 'Haymitch', 'Katniss']
assert intersect(data1, data2) == True
