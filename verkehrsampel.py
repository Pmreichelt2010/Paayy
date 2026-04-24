from gturtle import *

makeTurtle()
hideTurtle()

# Schwarzes Rechteck (gefuellt, mit scharfen Ecken)
setPenColor("black")
setFillColor("black")
setPenWidth(1)
penUp()
setPos(-40, -100)
setHeading(90)
penDown()
startPath()
repeat 2:
    fd(200)
    rt(90)
    fd(80)
    rt(90)
fillPath()
penUp()

# Rotes Licht oben
setPos(0, 70)
setPenColor("red")
dot(50)

# Gelbes Licht in der Mitte
setPos(0, 0)
setPenColor("yellow")
dot(50)

# Grünes Licht unten
setPos(0, -70)
setPenColor("green")
dot(50)
