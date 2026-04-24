from gturtle import *

makeTurtle()
speed(10)
setPenWidth(2)

s = 5
for i in range(40):
    rest = i % 4
    if rest == 0:
        setPenColor("blue")
    elif rest == 1:
        setPenColor("red")
    elif rest == 2:
        setPenColor("yellow")
    else:
        setPenColor("green")
    fd(s)
    rt(90)
    s = s + 4
