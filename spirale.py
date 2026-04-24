from gturtle import *

makeTurtle()
setPenColor("blue")

s = 2
repeat 100:
    repeat 4:
        fd(s)
        rt(90)
    rt(6)
    s = s + 2
