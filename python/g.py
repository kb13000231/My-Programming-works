import turtle
from math import sqrt

wn = turtle.Screen()
a = turtle.Turtle()

def hex(a):
    for i in range(20):
        for j in range(6):
            a.forward(200-10*i)
            a.left(60)

a.forward(100+sqrt(2)*100)
a.left(120)
hex(a)
