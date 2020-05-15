#!/usr/bin/env python3

def mean(data):
    """Compute the mean of a \textcolor{red}{non-empty} list of numbers.
    
    Parameter:
        data: a list of numbers
        
    Return value: the mean of the numbers in data
                  or None if data is empty
    """
    
    if len(data) == 0:
        return None
        
    sum = 0
    for item in data:
        sum = sum + item
    return sum / len(data)

def main():
    sales = [32, 42, 11, 15, 58, 44, 16]
    averageSales = mean(sales)
    print('Average daily sales were', averageSales)
    
main()
