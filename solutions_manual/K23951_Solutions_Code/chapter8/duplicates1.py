#!/usr/bin/env python3

def linearSearch(data, target):
    """Find the index of the first occurrence of target in data.
    
    Parameters:
        data: a list object to search in
        target: an object to search for
        
    Return value: the index of the first occurrence of target in data
    """

    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1

def linearSearchAll(data, target, start):
    """Find the indices of all occurrences of target in data.
    
    Parameters:
        data: a list object to search in
        target: an object to search for
        start: the index in data to start searching from
        
    Return value: a list of indices of all occurrences of 
                  target in data
    """

    found = [ ]
    for index in range(start, len(data)):
        if data[index] == target:
            found.append(index)
    return found
    

def removeDuplicates1(data):
    """Return a list containing only the unique items in data.
    
    Parameter:
        data: a list
        
    Return value: a new list of the unique values in data, 
                  in their original order
    """

    duplicateIndices = [ ]
    unique = [ ]
    for index in range(len(data)):
        if linearSearch(duplicateIndices, index) == -1:
            positions = linearSearchAll(data, data[index], index + 1)
            duplicateIndices.extend(positions)
            unique.append(data[index])
    return unique
    
def removeDuplicates2(data):
    """ (docstring omitted) """

    unique = [ ]
    for item in data:
        if linearSearch(unique, item) == -1:
            unique.append(item)
    return unique
    
def removeDuplicates3(data):
    """ (docstring omitted) """

    seen = { }
    unique = [ ]
    for item in data:
        if item not in seen:
            unique.append(item)
            seen[item] = True
    return unique

def main():
    letters = ['A', 'B', 'C', 'B', 'D', 'A', 'D', 'B']
    uniqueLetters = removeDuplicates3(letters)
    print(uniqueLetters)
    
main()
