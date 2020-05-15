#!/usr/bin/env python3

def minDay(data):
    """Compute the index of the minimum value in a non-empty list.
    
    Parameter:
        data: a list of numbers
        
    Return value: the index of the minimum value in data 
                  or -1 if data is empty
    """
    
    if len(data) == 0:
        return -1
        
    minI = 0
    for index in range(1, len(data)):
        if data[index] < data[minI]:
            minI = index
            
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[minI]

def main():
    sales = [32, 42, 11, 15, 58, 44, 16]
    day = minDay(sales)
    print('Minimum daily sales occurred on', day)
    
main()
