#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

import random, math

def montecarlo(f, a, b, n):
    s = 0
    for i in range(n):
        x = random.uniform(a, b)
        s += f(x)
    return s * (b-a)/n

def f(x):
    return math.sqrt(1-x**2)

