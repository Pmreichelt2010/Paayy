from gturtle import *
import random

makeTurtle()
speed(0)
hideTurtle()

# Drei verschiedene Farbpaletten
farben_bunt = ["red", "blue", "green", "yellow", "magenta",
               "cyan", "orange", "purple", "pink", "lime",
               "violet", "turquoise"]

farben_rot = ["red", "magenta", "purple", "pink", "crimson",
              "darkred", "hotpink", "deeppink", "mediumvioletred"]

farben_gruen = ["green", "blue", "cyan", "teal", "lime",
                "turquoise", "darkgreen", "darkcyan", "seagreen",
                "mediumseagreen"]


def zufallsquadrat(cx, cy, farben):
    x = cx + random.randint(-60, 60)
    y = cy + random.randint(-60, 60)
    s = random.randint(15, 45)
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


def kunstwerk(cx, cy, farben):
    repeat 40:
        zufallsquadrat(cx, cy, farben)


# Drei Kunstwerke nebeneinander in verschiedenen Stilen
kunstwerk(-140, 0, farben_bunt)
kunstwerk(0, 0, farben_rot)
kunstwerk(140, 0, farben_gruen)
