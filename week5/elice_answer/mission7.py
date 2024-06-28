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


t.speed("fast")
t.bgcolor("yellow")
t.penup()

# body
t.goto(-50, 50)
rect(100, 100, "green")

# legs
t.goto(10, -50)
rect(20, 40, "grey")
t.goto(-30, -50)
rect(20, 40, "grey")

# arms
t.goto(50, 40)
rect(40, 20, "grey")
t.goto(90, 70)
rect(20, 50, "grey")
t.goto(-90, 40)
rect(40, 20, "grey")
t.goto(-110, 40)
rect(20, 50, "grey")

# neck
t.goto(-20, 60)
rect(40, 10, "grey")

# head
t.goto(-40, 100)
rect(80, 40, "green")

################################################

# feet
t.goto(5, -90)
rect(40, 20, "pink")
t.goto(-45, -90)
rect(40, 20, "pink")

# hand
t.goto(85, 70)
rect(30, 10, "blue")
t.goto(85, 80)
rect(10, 10, "blue")
t.goto(105, 80)
rect(10, 10, "blue")
t.goto(-115, -10)
rect(30, 30, "pink")

# ears
t.goto(10, 120)
rect(20, 20, "pink")
t.goto(-30, 120)
rect(20, 20, "pink")


########################################


# eyes
t.goto(-30, 95)
rect(60, 20, "white")
t.goto(-30, 95)
rect(10, 10, "black")
t.goto(10, 85)
rect(10, 10, "black")

# mouth
t.goto(-30, 70)
t.right(10)
rect(60, 5, "red")
t.left(10)

# finger
t.goto(-125, -25)
rect(10, 10, "black")
t.goto(-85, -25)
rect(10, 10, "black")
t.goto(-115, -40)
rect(8, 10, "black")
t.goto(-104, -40)
rect(8, 10, "black")
t.goto(-93, -40)
rect(8, 10, "black")
