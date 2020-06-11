import random
from pair import Pair
from vector import Vector
import turtle

TURN_ANGLE = 30

PREV_WEIGHT = 0.5
# Boids model says decrease rule weight in order of rule number:
AVOID_WEIGHT = 0.25 # Avoid collisions is rule #1, weighted highest
MATCH_WEIGHT = 0.15 # Then rule #2, matching neighbors' velocities
CENTER_WEIGHT = 0.1 # Then rule #3, trying to move toward center of flock
# Weights need not sum to 1 because resulting vector is scaled to a unit vector

AVOID_DISTANCE = 3 # avoid only close neighbors
AVOID_ANGLE = 300

MATCH_DISTANCE = 10 # match velocity of intermediate neighbors
MATCH_ANGLE = 240

CENTER_DISTANCE = 15 # move toward center of farther neighbors
CENTER_ANGLE = 180 

class Boid:
    """A boid in an agent-based flocking simulation."""

    def __init__(self, myworld):
        """Construct a boid at a random position in the given world.

        Args:
            myworld (World object): a World object.
        """

        self._world = myworld
        (x, y) = (random.randrange(self._world.get_width()),
                  random.randrange(self._world.get_height()))
        while self._world[x, y] != None:
            (x, y) = (random.randrange(self._world.get_width()),
                      random.randrange(self._world.get_height()))
        self._position = Pair(x, y)
        self._world[x, y] = self
        self._velocity = Vector((random.uniform(-1, 1),
                                 random.uniform(-1, 1))).unit()
        self._turtle = turtle.Turtle()
        self._turtle.speed(0)
        self._turtle.up()
        self._turtle.setheading(self._velocity.angle())

    def move(self):
        """Move self to a new position in its world, by adding the x and y
        coordinates of its velocity vector to the x, y coordinates of its
        current position."""

        width = self._world.get_width()
        height = self._world.get_height()

        new_x = self._position[0] + self._velocity[0]
        new_x = min(max(0, new_x), width - 1)
        new_y = self._position[1] + self._velocity[1]
        new_y = min(max(0, new_y), height - 1)

        if self._world[new_x, new_y] == None:
            self._world[new_x, new_y] = self
            del self._world[self._position.get()]
            self._position = Pair(new_x, new_y)
            self._turtle.goto(new_x, new_y)

        # If the boid is approaching a boundary of world, have it turn
        #   in the next step:
        if (self._velocity[0] < 0 and new_x < 5) or \
           (self._velocity[0] > 0 and new_x > width - 5) or \
           (self._velocity[1] < 0 and new_y < 5) or \
           (self._velocity[1] > 0 and new_y > height - 5):
            # 13.4.3--have it randomly turn either left or right when approaching
            #   a boundary:
            if random.random() < 0.5:
                self._velocity.turn(TURN_ANGLE)
            else:
                self._velocity.turn(-TURN_ANGLE)
##            self._velocity.turn(TURN_ANGLE) # Turn angle is a constant in the sim

    def step(self):
        """Advance self one step in the flocking simulation."""

        new_velocity = (self._velocity * PREV_WEIGHT +
                        self._avoid() * AVOID_WEIGHT + # rule 1 avoid collisions
                        self._match() * MATCH_WEIGHT + # rule 2 try to match neighbors' velocity
                        self._center() * CENTER_WEIGHT) # rule 3 try to move toward center
        # 13.4.2:
            # my way:
##        if new_velocity == self._velocity:
##            new_angle = random.uniform(0, 360)
##            new_velocity.turn(new_angle)

        # Book's:
        if new_velocity == self._velocity:
            if random.random() < 0.2: # book wanted it to be RNG as to whether
                # angle gets changed at all. 0.2 is an arbitrary value "some probability"
                new_velocity = self._velocity + Vector((random.uniform(-0.1, 0.1),
                                                        rantom.uniform(-0.1, 0.1)))

        self._velocity = new_velocity.unit()
        self.move()

    def neighbors(self, distance, angle):
        """Return a list of boids within distance and viewing angle.

        Returns:
            (list): a list of Boid objects
        """

        neighbors = self._world.neighbors(self._position.get(), distance)
        visible_neighbors = []
        for boid in neighbors:
            neighbor_dir = Vector((boid._position - self._position).get())
            if self._velocity.diff_angle(neighbor_dir) < angle:
                visible_neighbors.append(boid)
        return visible_neighbors

    def _match(self):
        """Return the average velocity of neighboring boids."""
        neighbors = self.neighbors(MATCH_DISTANCE, MATCH_ANGLE)
        if len(neighbors) == 0:
            return Vector() # if no neighbors, no vector
        sum_velocity = Vector()
        for boid in neighbors:
            sum_velocity = sum_velocity + boid._velocity
        return (sum_velocity / len(neighbors)).unit()

    def _avoid(self):
        """Return a velocity away from close neighbors."""

        neighbors = self.neighbors(AVOID_DISTANCE, AVOID_ANGLE)
        if len(neighbors) == 0:
            return Vector()
        sum_position = Pair()
        for boid in neighbors: # Want the avg position in order to set a new
            #   vector that moves away most efficiently
            sum_position = sum_position + boid._position
        avg_position = sum_position / len(neighbors)

        avoid_velocity = Vector((self._position - avg_position).get())
        return avoid_velocity.unit()

    def _center(self):
        """Return a velocity toward center of neighboring flock."""
        # Like _avoid, except want to go toward this average instead of away
        #   from it

        neighbors = self.neighbors(CENTER_DISTANCE, CENTER_ANGLE)
        if len(neighbors) == 0:
            return Vector()
        sum_position = Pair()
        for boid in neighbors:
            sum_position = sum_position + boid._position
        avg_position = sum_position / len(neighbors)

        center_velocity = Vector((avg_position - self._position).get())
        return center_velocity.unit()
        

