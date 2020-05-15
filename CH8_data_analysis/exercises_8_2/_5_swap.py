def swap(data, i, j):
    """Swaps the positions of the items with indices i and j in list data.

    Returns:
        None
    """
    orig_i = data[i]
    data[i] = data[j]
    data[j] = orig_i


def main():
    data = ['fat', 'it', 'delete']
    swap(data, 0, 2)
    print(data)
    assert data == ['delete', 'it', 'fat'], f"fail, {data}"

if __name__ == '__main__':
    main()
    
