from gturtle import *
from random import randint

colors = ["red", "blue", "yellow", "lime", "magenta"]
points = []

def drawDot():
    i = randint(0, 4)
    c = colors[i]
    setPenColor(c)
    setFillColor(c)
    clean()
    for p in points:
        penUp()
        setPos(p[0], p[1])
        dot(30)

def addPoint(x, y):
    points.append((x, y))
    drawDot()

makeTurtle(mousePressed=addPoint)
speed(0)
hideTurtle()
