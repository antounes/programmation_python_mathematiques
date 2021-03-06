#!/home/antounes/anaconda3/bin/python3
#-*- coding: Utf-8 -*-

'''
    Module pour afficher une liste longue
'''

def lprint(liste, largeur, forme):
    n = len(liste)
    lignes = int(n/largeur)
    print('[', end='')
    for i in range(n):
        s = '{:' + forme + '}'
        if i != n-1:
            print(s.format(liste[i]), end=',')
        else:
            print(s.format(liste[i]), end=' ]')
        if i!=0 and i % largeur == largeur - 1:
            print('\n', end='')
    print()

if __name__ == "__main__":
    l = list(range(100))
    print(l)
    lprint(l, 12, '3d')
