#!/usr/bin/env python3

def merge(left, right, merged):
    """Merge two sorted lists, named left and right, into
       one sorted list named merged.
    
    Parameters:
        left: a sorted list
        right: another sorted list
        merged: the merged sorted list
        
    Return value: None
    """
    
    merged.clear()   # clear contents of merged
    leftIndex = 0    # index in left
    rightIndex = 0   # index in right
    
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]: 
            merged.append(left[leftIndex])    # left value is smaller
            leftIndex = leftIndex + 1
        else: 
            merged.append(right[rightIndex])  # right value is smaller
            rightIndex = rightIndex + 1
        
    if leftIndex >= len(left):             # items remaining in right
        merged.extend(right[rightIndex:])
    else:                                  # items remaining in left
        merged.extend(left[leftIndex:])

def mergeSort(data):
    """Recursively sort a list in place in ascending order, 
       using the merge sort algorithm.
    
    Parameter:
        data: a list of values to sort
        
    Return value: None
    """
    
    n = len(data)
    if n > 1:
        mid = n // 2              # divide list in half
        left = data[:mid]
        right = data[mid:]
        mergeSort(left)           # recursively sort first half
        mergeSort(right)          # recursively sort second half
        merge(left, right, data)  # merge sorted halves into data
        
def main():
    data = [60, 30, 50, 20, 10, 70, 40]
    mergeSort(data)
    print(data)
    
main()