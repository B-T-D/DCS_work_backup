"""
Exercise 3.5.1
2020-03-28 19:24
"""

def sum(number_1, number_2):
    """
    Returns the sum of two numbers.

    Args:
        number_1 (int): An integer to use as one of the two operands.
        number_2 (int): An integer to use as one of the two operands.

    Returns:
        int: The sum of the two args.
    """
    return number_1 + number_2

def main():
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    print(sum(number_1, number_2))

main()
