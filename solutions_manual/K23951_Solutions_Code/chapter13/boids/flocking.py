#!/usr/bin/env python3

import turtle
from world import *
from boid import *

WIDTH = 100
HEIGHT = 100
NUM_BIRDS = 30
ITERATIONS = 2000

def main():
    worldTurtle = turtle.Turtle()
    screen = worldTurtle.getscreen()
    screen.setworldcoordinates(0, 0, WIDTH - 1, HEIGHT - 1)
    screen.tracer(NUM_BIRDS)
    worldTurtle.hideturtle()
    
    sky = World(WIDTH, HEIGHT)
    for index in range(NUM_BIRDS):
        bird = Boid(sky)
        
    for step in range(ITERATIONS):
        sky.stepAll()
            
    screen.update()
    screen.exitonclick()
    
main()
