from gturtle import *

def blumenblatt():
    setFillColor("red")
    startPath()
    repeat 2:
        fd(100)
        rt(45)
        fd(100)
        rt(135)
    fillPath()

makeTurtle()

repeat 8:
    blumenblatt()
    rt(45)
