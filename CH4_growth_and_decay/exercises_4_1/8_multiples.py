
def multiples(n):
    """Prints all the multiples of the parameter n between 0 and 100,
    inclusive."""

    # First do it the obvious to me way, with an if.

##    for i in range(1, 101):
##        if i % n == 0:
##            print(i)


    """Just need to set the step size to n, no if statement or modular arithmetic
    needed:"""
    for i in range(0, 101, n): # Printing every nth number is idential to
            #   printing multiples of n. 12*2 is 12+12, and so on.
        print(i)


def main():
    multiples(4)
    multiples(12)

main()
