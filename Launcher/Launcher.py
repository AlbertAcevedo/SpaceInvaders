# Space Invaders for beginners
import turtle
import os


# @@@ All functions here @@@
# Move the player
def move_left():
    x = player.xcor()
    x -= p_speed
    player.setx(x)


def move_right():
    x = player.xcor()
    x += p_speed
    player.setx(x)


def move_up():
    player.forward(p_speed)


def move_down():
    player.backward(p_speed)

# Set up screen
wn = turtle.Screen()
wn.bgcolor("darkblue")
wn.title("Space invaders")
turtle.setup(700, 700) # Screen size

# Draw border
bpen = turtle.Turtle()
bpen.speed(0)
bpen.color("white")
bpen.pensize(3)

# Lift pen so it doesn't draw lines while re-positioning
bpen.penup()
bpen.setposition(-300, -300)

# Start drawing
bpen.pendown()
for side in range(4):
    bpen.fd(600)
    bpen.lt(90)
bpen.hideturtle()

# Create the player
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
p_speed = 15

# Create keyboard bindings
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.listen()
# Keep window open until x is hit
wn.mainloop()
