import risar, os
from random import randint, random
from PyQt5.QtCore import *

barve = [Qt.white, Qt.black, Qt.red, Qt.green, Qt.blue, Qt.magenta, Qt.yellow, Qt.gray, Qt.darkRed]

krogi = []
vx = []
vy = []
risar.barvaOzadja(Qt.black)
for i in range(30):
    x, y = risar.nakljucne_koordinate()
    circle = risar.krog(x, y, 15, risar.nakljucna_barva())
    krogi.append(circle)
    vx.append(2+random() * 3)
    vy.append(2+random() * 3)

for i in range(1100):
    for i in range(len(krogi)):
        circle = krogi[i]
        circle.setPos(circle.x() + vx[i], circle.y() + vy[i])
        if not (0 < circle.x() < risar.maxX - 35):
            vx[i] = -vx[i]
        if not (0 < circle.y() < risar.maxY - 35):
            vy[i] = -vy[i]
    risar.cakaj(0.017)