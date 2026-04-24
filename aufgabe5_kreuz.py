from gturtle import *

makeTurtle()
setPenColor("red")
setFillColor("red")

# Zur linken unteren Ecke des oberen Arms laufen
penUp()
lt(90)
fd(25)
rt(90)
fd(25)
penDown()

# Rotes Kreuz mit einer repeat-Schleife zeichnen
startPath()
repeat 4:
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    fd(50)
    lt(90)
fillPath()
