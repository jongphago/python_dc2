import turtle as t


def rect(h, v, color):
    t.pendown()
    t.pensize(1)
    t.color(color)

    t.begin_fill()

    for i in range(2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)
    t.end_fill()
    t.penup()
