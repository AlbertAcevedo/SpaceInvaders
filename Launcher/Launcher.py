# Space Invaders for beginners


import turtle
import os

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

#Create the player
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Keep window open until x is hit
wn.mainloop()
