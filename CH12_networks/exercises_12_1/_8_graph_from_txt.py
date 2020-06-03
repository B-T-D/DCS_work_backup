def read_graph(filename):
    """Reads a text file that represents a graph in one link per line, returns
    an adjacency list as a python dictionary."""

    # Solman is cleaner (does file read and dict build in one for loop,
    # for line in file), not worth time to fully transcribe. Solman at 161.
        # Directed graph from 12.1.2 below is more similar to book's way.
    file = open(filename, mode='r', encoding='utf-8')
    links = []
    line = ' '
    while line != '':
        line = file.readline().rstrip()
        link = tuple(line)
        if link != ():
            links.append(link)
    graph = {}
    for link in links:
        # Neither is already in:
        if link[0] not in graph.keys() and link[1] not in graph.keys():
            graph[link[0]] = [link[1]]
            graph[link[1]] = [link[0]]
        # link[0] is already in keys but link[1] isn't:
        elif link[0] in graph.keys() and link[1] not in graph.keys():
            # Add [1] to values for [0]'s key:
            graph[link[0]].append(link[1])
            # make a new key for [1] with [0] as its value:
            graph[link[1]] = [link[0]]
        # Vice versa--[1] already in keys but [0] isn't:
        elif link[1] in graph.keys() and link[0] not in graph.keys():
            graph[link[1]].append(link[0])
            graph[link[0]] = [link[1]]
        # Both already in keys but not in each others' values:
        else:
            graph[link[0]].append(link[1])
            graph[link[1]].append(link[0])
            
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
    filename = 'graph.txt'
    graph = read_graph(filename)

    expected = {'A': ['B', 'C', 'D'],
                'B': ['A', 'E'],
                'C': ['A', 'D', 'E'],
                'D': ['A', 'C'],
                'E': ['B', 'C']}

    actual = graph

    print("--Actual--")
    for key, value in actual.items():
        print(f"{key} : {value}")

    print("--Expected--")
    for key, value in expected.items():
        print(f"{key} : {value}")

    assert actual == expected, f"actual {actual}, expected {expected}"


    print("------Directed graph version------")

    expected = {'A': ['B', 'C', 'D'],
                'B': ['E'],
                'C': ['D', 'E'],
                'D': [],
                'E': []}

    actual = read_directed_graph(filename)

    print("--Actual--")
    for key, value in actual.items():
        print(f"{key} : {value}")

    print("--Expected--")
    for key, value in expected.items():
        print(f"{key} : {value}")

    assert actual == expected, f"actual {actual}, expected {expected}"

main()
