#!/usr/bin/env python3

def insertionSort(data):
    """Sort a list of values in ascending order using the
       insertion sort algorithm.
    
    Parameter:
        data: a list of values
        
    Return value: None
    """
    
    n = len(data)
    for insertIndex in range(1, n):
        itemToInsert = data[insertIndex]
        index = insertIndex - 1
        while index >= 0 and data[index] > itemToInsert:
            data[index + 1] = data[index]
            index = index - 1
        data[index + 1] = itemToInsert

def main():
    data = [50, 30, 40, 20, 10, 70, 60]
    insertionSort(data)
    print(data)
    
main()
