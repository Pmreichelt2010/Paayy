from gturtle import *
import random

makeTurtle()
speed(0)
hideTurtle()

farben = ["red", "blue", "green", "yellow", "magenta",
          "cyan", "orange", "purple", "pink", "lime",
          "violet", "turquoise"]

def zufallsquadrat():
    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    s = random.randint(20, 80)
    c = random.choice(farben)

    setPenColor(c)
    setFillColor(c)
    penUp()
    setPos(x, y)
    penDown()
    startPath()
    repeat 4:
        fd(s)
        lt(90)
    fillPath()

repeat 60:
    zufallsquadrat()
