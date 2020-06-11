import math

def _distance(point1, point2):
    """Return the distance between two positions (2D points).

    Args:
        point1 (tuple): an x, y coordinate ordered pair
        point2 (tuple): a second x, y coordinate pair

    Returns:
        (float): Euclidean distance between the points
    """
    # Not a method of the World class because this func doesn't need to access
    #   any attributes of the class.
    diff_x = point1[0] - point2[0]
    diff_y = point1[1] - point2[1]
    return math.sqrt(diff_x ** 2 + diff_y ** 2)

class World:
    """A two-dimensional world class."""

    def __init__(self, width, height):
        """
        Args:
            width (int): the number of columns in the grid
            height (int): the number of rows in the grid
        """
        self._width = width
        self._height = height
        self._agents = {}

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def __getitem__(self, position):
        """Return the agent at the given position."""
        if position in self._agents:
            return self._agents[position]
        return None

    def __setitem__(self, position, agent):
        """Set the given position to contain agent."""

        if (position not in self._agents) and \
           (position[0] >= 0) and (position[0] < self._width) and \
           (position[1] >= 0) and (position[1] < self._height):
            self._agents[position] = agent

    def __delitem__(self, position):
        """Delete the agent at the given position."""

        if position in self._agents: # if there's an agent there
            del self._agents[position] # self._agents is a dict object so has del operator

    def neighbors(self, position, distance):
        """Return a list of agents within distance of position (a tuple).

        Returns:
            (list): a list of neighboring agents
        """

        neighbors = []
        for other_position in self._agents:
            if (position != other_position) and\
               (_distance(position, other_position) <= distance):
                neighbors.append(self._agents[other_position])
        return neighbors

    def step_all(self):
        """Advance all agents one step in the simulation."""

        agents = list(self._agents.values())
        for agent in agents:
            agent.step()

def main():

    myworld = World(10, 10)
    myworld[2, 1] = 5
    print(myworld[2, 1])
    myworld[2, 1] = 7 # won't change it if already occupied
    print(myworld[2, 1]) # output is still 5
    del myworld[2, 1]
    print(myworld[2, 1])

if __name__ == '__main__':
    main()
    
