from gturtle import *

farbe = "red"

def stern(x, y):
    global farbe
    penUp()
    setPos(x, y)
    setHeading(0)
    penDown()
    setPenColor(farbe)
    setFillColor(farbe)
    startPath()
    for i in range(5):
        fd(40)
        rt(144)
    fillPath()
    if farbe == "red":
        farbe = "blue"
    else:
        farbe = "red"

makeTurtle(mousePressed=stern)
speed(0)
hideTurtle()
