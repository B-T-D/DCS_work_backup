import turtle

def draw_regular_polygon(tortoise, side_length, num_sides):
    turn_angle = get_turn_angle(num_sides)
    print(turn_angle)
    for i in range(num_sides):
        tortoise.forward(side_length)
        tortoise.right(turn_angle)

def get_turn_angle(num_sides):
    return 180 - (((num_sides - 2) * 180) / num_sides)

def draw_circle(tortoise, radius):
    circumference = 2 * 3.14159 * radius
    side_length = circumference / 360
    draw_regular_polygon(tortoise, side_length, 360)

t = turtle.Turtle()
t.speed(9)

##sides = int(input("How many sides? >> "))

sides = 13

draw_regular_polygon(t, 4, sides)

draw_circle(t, 30)
