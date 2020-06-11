import turtle
import world as w
import boid as b

WIDTH = 100
HEIGHT = 100
NUM_BIRDS = 30
ITERATIONS = 2000

def main():
    world_turtle = turtle.Turtle()
    screen = world_turtle.getscreen()
    screen.setworldcoordinates(0, 0, WIDTH - 1, HEIGHT - 1)
    screen.tracer(NUM_BIRDS)
    world_turtle.hideturtle()

    sky = w.World(WIDTH, HEIGHT) # create the world
    for index in range(NUM_BIRDS): # create the boids in myworld=sky
        bird = b.Boid(sky)

    for step in range(ITERATIONS): # run the simulation
        sky.step_all()

    screen.update()
    screen.exitonclick()

if __name__ == '__main__':
    main()
