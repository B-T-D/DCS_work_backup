#!/usr/bin/env python3

def adjust(rates):
    """Subtract one percent (0.01) from each rate in a list.
    
    Parameter:
        rates: a list of numbers representing rates (percentages)
        
    Return value: None
    """
    
    for index in range(len(rates)):
        rates[index] = rates[index] - 0.01
	    
def main():
    unemployment = [0.053, 0.071, 0.065, 0.074]
    adjust(unemployment)
    print(unemployment)
    
main()
