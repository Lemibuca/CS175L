
#CS 175L
#LESLIE BUSTAMANTE
#STOP SIGN

import math
import turtle

#Named constants

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

# size the winfow
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

#Calculate the diameter of the octagon

s = LENGTH
x = s/math.sqrt(2)
diameter = s + (2 * x)

#Starting point
#Draw the octagon
t = turtle.Turtle()
t.color('red')
t.shape('turtle')
t.begin_fill()
for i in range(NUM_SIDES):
    t.forward (s)
    t.left (ANGLE)
t.end_fill()
t.goto(7,15)
t.color('white')
t.width(10)
for x in range(NUM_SIDES):
    t.forward (88)
    t.left (ANGLE)

#Display stop
fontSize = 45
t.penup()
t.goto(51,85)
t.color('white')
t.write("STOP", align = "center", font = ("Arial", fontSize, "bold"))
t.pendown()

turtle.done()


