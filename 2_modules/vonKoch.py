#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

import turtle
turtle.pen(speed=0) #vitesse maximale

def von_koch(longueur, n):
    if n == 1:
        turtle.forward(longueur)
    else:
        d = longueur/3.
        von_koch(d, n-1); turtle.left(60)
        von_koch(d, n-1); turtle.right(120)
        von_koch(d, n-1); turtle.left(60)
        von_koch(d, n-1)

def flocon(longueur, n):
    turtle.up()
    turtle.goto(-longueur/2, longueur/3) #on se place en haut à gauche
    turtle.down()

    for i in range(3):
        von_koch(longueur, n); turtle.right(120)

flocon(300, 6)
