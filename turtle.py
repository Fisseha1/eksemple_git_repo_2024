# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:23:18 2024

@author: Fisseha Araya
"""

import turtle
import math


# Initial setup
t = turtle.Turtle()
t.speed(1)  # Set the speed of the turtle

# Draw the first line
t.forward(100)

# Turn and draw the second line
t.right(90)
t.forward(50)

# Move without drawing
t.penup()
t.forward(50)
t.pendown()

# Set pen color, size, and fill color
t.pencolor("orange")
t.pensize(5)
t.fillcolor("green")
# Start filling the shape
t.begin_fill()

# Draw a triangle
for _ in range(3):
    t.forward(100)
    t.right(120)

# End filling the shape
t.end_fill()

# Finish
turtle.done()