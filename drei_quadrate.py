from gturtle import *

def square(s, c):
    setPenColor(c)
    setFillColor(c)
    startPath()
    repeat 4:
        fd(s)
        lt(90)
    fillPath()

makeTurtle()

square(150, "yellow")
square(100, "red")
square(50, "green")
