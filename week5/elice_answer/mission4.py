import turtle as t


def rect(h, v):
    for i in range(2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)


h = 100
v = 80
t.pensize(1)
t.speed("fastest")
rect(h, v)

t.penup()
t.goto(-100, -100)
t.pendown()
t.color("red")
t.bgcolor("blue")

h = 200
v = 20
t.pensize(10)
t.speed("slowest")
t.begin_fill()
rect(h, v)
t.end_fill()
