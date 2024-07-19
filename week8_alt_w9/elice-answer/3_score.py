import turtle as t


# Define the functions move_up, move_down, move_left, and move_right, start
def move_up():
    me.setheading(90)


def move_down():
    me.setheading(270)


def move_left():
    me.setheading(180)


def move_right():
    me.setheading(0)


# TODO: Add the print statement
def start():
    global score
    while True:
        me.forward(1)
        if me.distance(apple) < 20:
            score += 10
            pass  # Add the print statement here


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

# TODO: Create a turtle object: score_turtle
score_turtle = None
pass  # ht
pass  # penup
x = t.window_height() / 3
y = t.window_width() / 3
pass  # setpos

# TODO: Initialize the score
pass  # score

# Register the functions to the corresponding keys
t.onkey(start, "space")
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")

# Listen for the events
t.listen()


t.mainloop()
