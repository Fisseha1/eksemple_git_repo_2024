# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:23:18 2024

@author: Fisseha Araya
"""

import turtle
import math

def tegn_trekant(pennsize=9,penncolor="orange",fill="green"):
    turtle.pencolor(penncolor)
    turtle.pensize(pennsize)
    turtle.fillcolor(fill)
    turtle.begin_fill()
        
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.end_fill()
tegn_trekant()
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
tegn_trekant(3,"black","blue")
turtle.done()