
def count(text, target):
    """Count the number of target strings in text.

    Args:
        text (str): A string object
        target (str): A string object.

    Returns:
        (int): Number of occurrences of target in text.
    """

    count = 0
    for index in range(len(text)):
        if text[index:index + len(target)] == target:
            count = count + 1
    return count

result = count('Diligence is the mother of good luck.', 'the')
print(result)
