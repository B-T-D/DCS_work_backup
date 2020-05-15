#!/usr/bin/env python3

def hanoi(n, source, destination, intermediate):
    """Print instructions for solving the Tower of Hanoi puzzle.
    
    Parameters:
        n: the number of disks
        source: the source peg
        destination: the destination peg
        intermediate: the other peg
        
    Return value: None
    """
    
    if n >= 1:
        hanoi(n - 1, source, intermediate, destination)
        print('Move a disk from peg', source, 'to peg', destination)
        hanoi(n - 1, intermediate, destination, source)

def main():
    hanoi(8, 'A', 'C', 'B')
    
main()
