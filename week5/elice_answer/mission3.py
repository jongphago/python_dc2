import turtle as t


def rect(h, v):
    for i in range(2):
        t.forward(h)
        t.right(90)
        t.forward(v)
        t.right(90)


h = 100
v = 80
rect(h, v)
