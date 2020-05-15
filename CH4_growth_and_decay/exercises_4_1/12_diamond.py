def diamond():
    """Prints asterisks in a pattern that leaves whitespace in a diamond shape."""

    for i in range(5, -1, -1): # Print the top half of the diamond
        print(
            ('*' * i) # Print first block of asterisks
              +
              (' ' * (11 - 2 * i))
              # Print number of spaces equal to total line characters (11), minus
              # the number of asterisks in the line (2 * i)
              +
              ('*' * i)# Print second block of asterisks
              )
    for i in range(1, 6): # Invert the first for loop to print the bottom half
        print(
            ('*' * i) +
            (' ' * (11 -2 * i)) +
            ('*' * i)
            )

diamond()
