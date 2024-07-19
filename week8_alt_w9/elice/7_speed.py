import turtle as t
import random as r


# Define the functions move_up, move_down, move_left, and move_right, start
def move_up():
    me.setheading(90)


def move_down():
    me.setheading(270)


def move_left():
    me.setheading(180)


def move_right():
    me.setheading(0)


# TODO: Adjust the speed of the turtle object
def start():
    global score
    apple_move()
    display_score()
    while True:
        me.forward(score / 10 + 1)
        if me.distance(apple) < 20:
            apple_move()
            score += 10
            display_score()
        if outside_window():
            game_over()
            break


# Define the function display_score
def display_score():
    score_turtle.clear()
    score_turtle.write(score, font=("Arial", 30, "bold"))


# Define the function apple_move
def apple_move():
    apple.ht()
    apple.setx(r.randint(-200, 200))
    apple.sety(r.randint(-200, 200))
    apple.st()


# Define the function outside_window
def outside_window():
    (x, y) = me.pos()
    is_outside = (
        x > t.window_width() / 2
        or x < -t.window_width() / 2
        or y > t.window_height() / 2
        or y < -t.window_height() / 2
    )
    return is_outside


# Define the function game_over
def game_over():
    score_turtle.clear()
    score_turtle.write("Game\nOver", font=("Arial", 30, "normal"))


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

# Create a turtle object: score_turtle
score_turtle = t.Turtle()
score_turtle.ht()
score_turtle.penup()
x = t.window_height() / 3
y = t.window_width() / 3
score_turtle.setpos(x, y)

# Initialize the score
score = 0

# Register the functions to the corresponding keys
t.onkey(start, "space")
t.onkey(move_up, "Up")
t.onkey(move_down, "Down")
t.onkey(move_left, "Left")
t.onkey(move_right, "Right")

# Listen for the events
t.listen()


t.mainloop()
