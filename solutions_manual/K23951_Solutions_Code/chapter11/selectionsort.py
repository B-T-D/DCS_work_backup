#!/usr/bin/env python3

def swap(data, i, j):
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

def selectionSort(data):
    """Sort a list of values in ascending order using the
       selection sort algorithm.
    
    Parameter:
        data: a list of values
        
    Return value: None
    """
    
    n = len(data)
    for start in range(n - 1):
        minIndex = start
        for index in range(start + 1, n):
            if data[index] < data[minIndex]:
                minIndex = index
        if minIndex != start:
            swap(data, start, minIndex)

def main():
    numbers = [50, 30, 40, 20, 10, 70, 60]
    animals = ['dog', 'cat', 'monkey', 'zebra', 'platypus', 'armadillo']
    heights = [7.80, 6.42, 8.64, 7.83, 7.75, 8.99, 9.25, 8.95]

    selectionSort(numbers)
    print(numbers)
    selectionSort(animals)
    print(animals)
    selectionSort(heights)
    print(heights)
    
main()
