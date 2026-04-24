from gturtle import *

makeTurtle()
# Turtle startet in der Mitte und schaut nach oben (Norden).

# Zur linken unteren Ecke des Rechtecks laufen
penUp()
bk(100)
lt(90)
fd(40)
rt(90)
penDown()

# Schwarzes Rechteck (80 breit, 200 hoch)
setPenColor("black")
setFillColor("black")
startPath()
fd(200)
rt(90)
fd(80)
rt(90)
fd(200)
rt(90)
fd(80)
fillPath()

# Zur Position des gruenen Lichts laufen
penUp()
rt(90)
fd(30)
rt(90)
fd(40)
lt(90)

# Gruenes Licht unten
setPenColor("green")
dot(50)

# Gelbes Licht in der Mitte
fd(70)
setPenColor("yellow")
dot(50)

# Rotes Licht oben
fd(70)
setPenColor("red")
dot(50)
