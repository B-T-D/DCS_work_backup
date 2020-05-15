def triangle3():
    """Uses a for loop to print right-aligned asterisks in the shape of a
    downward-pointing right triangle."""

    for i in range(6, 0, -1):
        print('{:<}'.format(i * '*'))
        # ^^ This aligns wrong side

    # Book does it without the string formatting:
    print("Book's way:")
    for count in range(6, 0, -1):
        print(' ' * (6 - count) + '*' * count) # Prints a descending number of
            #   blank spaces before the first asterisk

    
        

triangle3()
