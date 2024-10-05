# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:23:18 2024

@author: Fisseha Araya
"""

import turtle
import math

def tegn_3kant(pennsize=9,penncolor="orange",fill="green"):
    turtle.pencolor(penncolor)
    turtle.pensize(pennsize)
    turtle.fillcolor(fill)
    turtle.begin_fill()
        
    turtle.forward(130)
    turtle.right(120)
    turtle.forward(130)
    turtle.right(120)
    turtle.forward(130)
    turtle.end_fill()
tegn_3kant()
turtle.penup()
turtle.goto(-130,130)
turtle.pendown()
tegn_3kant(3,"red","blue")
turtle.done()