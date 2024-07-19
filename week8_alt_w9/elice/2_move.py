import turtle as t


# TODO: Define the functions move_up, move_down, move_left, and move_right
def move_up():
    me.setheading(90)


def move_down():
    pass


def move_left():
    pass


def move_right():
    pass


# TODO: define the function start
def start():
    while True:
        pass  # forward


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
t.onkey(move_up, "Up")  # up
pass  # down
pass  # left
pass  # right

# TODO: Listen for the events
t.listen()


t.mainloop()
