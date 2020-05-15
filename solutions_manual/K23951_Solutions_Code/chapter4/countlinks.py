#!/usr/bin/env python3

def countLinks(totalNodes):
    """Prints a table with the maximum total number of links 
       in networks with 2 through totalNodes nodes.
    
    Parameter:
        totalNodes: the total number of nodes in the network
        
    Return value: 
        the maximum number of links in a network with totalNodes nodes
    """
    
    totalLinks = 0
    for node in range(2, totalNodes + 1):
        newLinks = node - 1
        totalLinks = totalLinks + newLinks
        print(node, newLinks, totalLinks)

    return totalLinks
    
def main():
    links = countLinks(10)
    print('The total number of links is', links)
    
main()
