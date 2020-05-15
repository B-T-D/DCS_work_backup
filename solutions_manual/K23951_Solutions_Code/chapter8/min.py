#!/usr/bin/env python3

def min(data):
    """Compute the minimum value in a non-empty list of numbers.
    
    Parameter:
        data: a list of numbers
        
    Return value: the minimum value in data or None if data is empty
    """
    
    if len(data) == 0:
        return None
    
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
    
def main():
    sales = [32, 42, 11, 15, 58, 44, 16]
    minSales = min(sales)
    print('Minimum daily sales were', minSales)
    
main()
