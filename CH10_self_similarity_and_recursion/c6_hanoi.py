def hanoi(n, source, destination, intermediate):
    """
    Print instructions for solving the Tower of Hanoi puzzle.
    Args:
        n (int): the number of disks
        source (str): the source peg
        destination (str): the destination peg
        intermediate (str): the other peg neither source nor dest

    Returns:
        None
    """
    if n >= 1:
        hanoi(n - 1, source, intermediate, destination)
        print('Move a disk from peg', source, 'to peg', destination)
        input('press enter to continue after instruction executed')
        hanoi(n - 1, intermediate, destination, source)

hanoi(6, "1", "3", "2")
print("completed")
        
    
