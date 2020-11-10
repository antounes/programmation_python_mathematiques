#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

from time import time
from math import sin

def f1(n):
    liste = []
    for i in range(n):
        liste += [sin(i)]
    return liste

def f2(n):
    liste = []
    for i in range(n):
        liste.append(sin(i))
    return liste

def f3(n):
    return [sin(i) for i in range(n)]

def durée(fonction, n=10000000):
    debut = time()
    fonction(n)
    fin = time()
    return fin - debut

print(' {:-<25}> {:f} s'.format('utilisation de += ', durée(f1)))
print(' {:-<25}> {:f} s'.format('utilisation de .append ', durée(f2)))
print(' {:-<25}> {:f} s'.format('liste en compréhension ', durée(f3)))
