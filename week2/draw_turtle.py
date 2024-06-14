import turtle


def draw_square(side=100):
    for i in range(4):
        t.forward(side)
        t.left(90)


def draw_rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)


def draw_polygon(n, side):
    for i in range(n):
        t.forward(side)
        t.left(360 / n)


t = turtle.Turtle()
t.shape("turtle")

draw_rectangle(40, 20)
