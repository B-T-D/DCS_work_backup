def adjust(rates):
    """Subtract one percent from each rate in a list.

    Args:
        rates (list): List of floats representing rates (percentages)

    Returns:
        None
    """
    for index in range(len(rates)):
        rates[index] = rates[index] - 0.01

def main():
    unemployment = [0.053, 0.071, 0.065, 0.074]
    adjust(unemployment)
    print(unemployment)

main()
