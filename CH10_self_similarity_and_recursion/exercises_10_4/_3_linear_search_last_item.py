def linear_search(data, target, last):
    """Looks at last item in the list, and recursively calls the function with
    the sublist not containing the last item (instead of first item)."""
    if (last < 0) or (last >= len(data)):
        return -1
    if target == data[last]:
        return last
    return linear_search(data, target, last - 1)



data = [1, 2, 3, 4, 567, 8, 9, 10, 11]
print(linear_search(data, 567, len(data) - 1))
print(linear_search(data, 'spam', len(data) - 1))
