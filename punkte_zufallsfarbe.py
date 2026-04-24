from gturtle import *
from random import randint

colors = ["red", "blue", "yellow", "lime", "magenta"]

def drawDot(x, y):
    i = randint(0, 4)
    c = colors[i]
    setPenColor(c)
    setFillColor(c)
    penUp()
    setPos(x, y)
    dot(30)

makeTurtle(mousePressed=drawDot)
speed(0)
hideTurtle()
