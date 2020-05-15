import turtle

def draw_regular_polygon(tortoise, side_length, num_sides):
    turn_angle = get_turn_angle(num_sides)
    print(turn_angle)
    for i in range(num_sides):
        tortoise.forward(side_length)
        tortoise.right(turn_angle)

def get_turn_angle(num_sides):
    return 180 - (((num_sides - 2) * 180) / num_sides)

t = turtle.Turtle()
t.speed(0)

##sides = int(input("How many sides? >> "))

sides = 3

draw_regular_polygon(t, 50, sides)
