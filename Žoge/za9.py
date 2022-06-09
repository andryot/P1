# coding=utf-8
import risar, os
from random import randint, random
import time
from PyQt5 import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox

krogi = []
vx = []
vy = []
risar.barvaOzadja(risar.crna)

for i in range(30):
    x, y = randint(0, risar.maxX - 20), randint(0, risar.maxY- 20)
    circle = risar.krog(x, y, 10, risar.nakljucna_barva())
    krogi.append(circle)
    vx.append(3 + random() * 2)
    vy.append(3 + random() * 2)

mis = risar.krog(risar.maxX / 2, risar.maxY / 2 , 30)

izbrisane = []

kroglica_not_hit = 1
mouse_not_pressed_yet = 1
stevec_zadetih = 0

for i in range(1000):
    j = 0
    while j < len(krogi):
        circle = krogi[j]
        circle.setPos(circle.x() + vx[j], circle.y() + vy[j])

        if not (0 < circle.x() < risar.maxX - 15):
            vx[j] = -vx[j]
        if not (0 < circle.y() < risar.maxY - 15):
            vy[j] = -vy[j]
        if risar.klik and mouse_not_pressed_yet:
            mouse_not_pressed_yet = 0
            izbrisane.append([mis, time.time()])

        if not risar.klik:
            x, y = risar.miska
            mis.setPos(x, y)

        elif kroglica_not_hit and mis.collidingItems() and mis.collidesWithItem(circle):
            kroglica_not_hit = 0
            izbrisane.append([circle, time.time()])

            circle.setRect(-30, -30, 60, 60)
            c = circle.pen().color().lighter()
            c.setAlpha(192)
            circle.setBrush(c)

            krogi.pop(j)
            vx.pop(j)
            vy.pop(j)
            stevec_zadetih += 1
            j -= 1

        elif [x  for x, _ in izbrisane if circle.collidesWithItem(x)]:
            izbrisane.append([circle, time.time()])

            circle.setRect(-30, -30, 60, 60)
            c = circle.pen().color().lighter()
            c.setAlpha(192)
            circle.setBrush(c)

            krogi.pop(j)
            vx.pop(j)
            vy.pop(j)
            stevec_zadetih += 1

            j -= 1

        if risar.klik:
            for l, x in enumerate(izbrisane):
                if time.time() - x[1] > 4:
                    risar.odstrani(x[0])
                    izbrisane.pop(l)

            if len(krogi) == 30 and not mouse_not_pressed_yet and len(izbrisane) == 0:
                QMessageBox.information(None, "Obvestilo", f"Žal ti ni uspelo")
                risar.stoj()
        j += 1
    risar.cakaj(0.02)
    if len(krogi) == 0:
        QMessageBox.information(None, "Obvestilo", f"Bravo zadel si vseh {stevec_zadetih} zog")
        risar.stoj()

    elif len(izbrisane) == 0 and len(krogi) != 30:
        QMessageBox.information(None, "Obvestilo", f"Razstrelil {stevec_zadetih} žog od 30")
        risar.stoj()
QMessageBox.information(None, "Obvestilo", f"Zmanjkalo ti je časa")
risar.stoj()