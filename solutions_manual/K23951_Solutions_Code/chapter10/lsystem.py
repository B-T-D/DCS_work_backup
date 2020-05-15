#!/usr/bin/env python3
    
def derive(string, productions, depth):
    """Recursively apply productions to axiom 'depth' times.
    
    Parameters:
        string: a string of L-system symbols
        productions: a dictionary containing L-system productions
        depth: the number of times the productions are applied
        
    Return value:
        the new string reflecting the application of productions
    """
    
    if depth <= 0:        # base case
        return string
        
    newString = ''        # beginning of recursive case
    for symbol in string:
        if symbol in productions:
            newString = newString + productions[symbol]
        else:
            newString = newString + symbol
    return derive(newString, productions, depth - 1)

def main():
    rules = {'X': 'F[-X]+X', 'F': 'FF'}
    result = derive('X', rules, 3)
    print(result)
    
main()
