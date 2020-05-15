def square(letter, width):
    """
    Args:
        letter (str): A single letter
        width (int): The number of times each letter character should be printed
            to make up the width of the square. 
    """
##    for i in range(width):
##        print_string = ''
##        for i in range(width):
##            print_string += letter
##        print(print_string)

    # You can use the multiplication operator on strings:
    for line in range(width):
        print(letter * width)


square('Q', 5)
