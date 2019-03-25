# Space Invaders for beginners
import turtle
import time


# @@@ All functions here @@@
# Check boundaries
def in_bounds(var):
    if var < -280:
        var = -280
    if var > 280:
        var = 280
    return var


# Move the player
def move_left():
    x = player.xcor()
    x -= p_speed
    x = in_bounds(x)
    player.setx(x)


def move_right():
    x = player.xcor()
    x += p_speed
    x = in_bounds(x)
    player.setx(x)


def move_up():
    player.forward(p_speed)
    y = in_bounds(player.ycor())
    player.sety(y)


def move_down():
    player.backward(p_speed)
    y = in_bounds(player.ycor())
    player.sety(y)


# Move the enemy
def move_enemy(speed):
    x = enemy.xcor()
    x += speed
    enemy.setx(x)


def incoming_enemy():
    y = enemy.ycor()
    for i in range(4):
        y -= 10
        time.sleep(0.01)
        enemy.sety(y)


def main_loop():
    e_speed = 2
    while True:
        move_enemy(e_speed)
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            e_speed *= -1
            incoming_enemy()


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

# Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(0,250)


# Create keyboard bindings
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.listen()

# Start game
main_loop()


