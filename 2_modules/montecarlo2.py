#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

import random
import sys

from math import sqrt, hypot, pi

def f(x, y, a, b):
    c = sqrt(a**2 - b**2)
    return hypot(x-c, y) + hypot(x+c, y)

def montecarlo2(a, b, n):
    xrandom = [random.uniform(-a, a) for i in range(n)]
    yrandom = [random.uniform(-b, b) for i in range(n)]


    s = sum(f(x, y, a, b) for x in xrandom
            for y in yrandom if hypot(x/a, y/b) <= 1) 
            
    return s * (4 * a * b) / n**2

print('-'*63)
print('{0:>7s} | {1:^15s} | {2:^15s} | {3:^15s} |'.format('n',
      'approximation', 'erreur absolue', 'erreur relative'))
print('-'*63)

for i in range(1, 5):
    a, b, n = 2, 1, 10**i
    approx = montecarlo2(a, b, n)
    val_exacte = 2*pi*b*(3*a**2-b**2)/3
    erreur = val_exacte - approx
    erreur_relative = abs((val_exacte - approx)/val_exacte)
    print('{0:7d} | {1: 15.10f} | {2:^ 15.3e} | {3:^ 15.3e} |'
          .format(n, approx, erreur, erreur_relative),
          file=sys.stdout, flush=True)
print('-'*63) 
