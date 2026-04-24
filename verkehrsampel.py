from gturtle import *

makeTurtle()
hideTurtle()

# Schwarzes Rechteck mit Stiftbreite 80
setPenColor("black")
setPenWidth(80)
penUp()
setPos(0, -100)
penDown()
setPos(0, 100)
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
