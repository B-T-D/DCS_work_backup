import matplotlib.pyplot as pyplot

def count_links(total_nodes):
    """Prints a table with the maximum total number of links in networks with
    2 through total_nodes nodes.

    Args:
        total_nodes: The total number of nodes in the network.

    Returns:
        (int): Maximum number of links in a network with total_nodes nodes.
    """

    total_links = 0
    print('Node | New Links | Total Links')
    for node in range(2, total_nodes + 1):
        new_links = node - 1
        total_links = total_links + new_links
        
        print('{} | {} | {}'.format(node, new_links, total_links))

    return total_links

def plot_links(total_nodes):
    total_links = 0
    links_list = [total_links]
    for node in range(2, total_nodes + 1):
        new_links = node - 1
        total_links = total_links + new_links
        links_list.append(total_links)
    
    pyplot.plot(range(1, total_nodes + 1), links_list) # total nodes on x axis, max links on y axis)
    pyplot.xlabel('Total nodes')
    pyplot.ylabel('Maximum total links')
    pyplot.show()
    
def main():
    plot_links(total_nodes=1000)

main()
