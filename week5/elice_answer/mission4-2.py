import time
import turtle as t


def rect(h, v, my_width=None, my_color="black"):
    t.pendown()
    t.pensize(width=my_width)
    t.color(my_color)
    for i in range(2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)
    t.penup()


rect(100, 80, my_width=1)
t.goto(-100, -100)
rect(200, 20, my_width=10, my_color="red")

time.sleep(2)
