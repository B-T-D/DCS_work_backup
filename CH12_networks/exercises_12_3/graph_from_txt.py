"""Using the solution manual's version for the exercises, because SM and the
files on the book site have a space between the characters in each line of the
txt."""

def read_graph(filename):
    """Reads a text file that represents a graph in one link per line, returns
    an adjacency list as a python dictionary."""

    file = open(filename, mode='r', encoding='utf-8')
    graph = {}
    for line in file:
        edge = line.split()
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    file.close()
    return graph

def read_directed_graph(filename):
    """Same as above, but interprets the graph as directed. E.g. if the text
    file line is 'AB' that means one-way route from A to B without necessarily
    a reciprocal B to A link."""
    # Book's version returns a dict with no keys for the non-sender (non-origin) nodes.
    # Mine returns a blank list.

    file = open(filename, mode='r', encoding='utf-8')
    graph = {}
    for line in file:
        edge = list(line.rstrip())
        print(f"edge is {edge}")
        if edge[0] in graph:
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] not in graph: # Remove this to return dict that only has keys for origin nodes
            graph[edge[1]] = []
        print(f"updated graph to {graph}")

    return graph

def main():
    grid = read_graph('grid.txt')
    print(grid)

if __name__ == '__main__':
    main()
