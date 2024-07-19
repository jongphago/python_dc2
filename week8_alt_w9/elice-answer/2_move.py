import turtle as t


# TODO: Define the functions move_up, move_down, move_left, and move_right
def move_up():
    me.setheading(90)


def move_down():
    me.setheading(270)


def move_left():
    me.setheading(180)


def move_right():
    me.setheading(0)


# TODO: define the function start
def start():
    while True:
        me.forward(1)


# Create a turtle object: me
me = t.Turtle()
me.shape("square")
me.color("blue")
me.penup()

# Create another turtle object: apple
apple = t.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()

# TODO: Register the functions to the corresponding keys
t.onkey(start, "space")
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")

# TODO: Listen for the events
t.listen()


t.mainloop()
