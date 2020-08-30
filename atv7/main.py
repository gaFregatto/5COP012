import numpy as np
import cv2 as cv
import sys
import os

from Point import *
TRINTA = np.pi/6
QC = np.pi/4
SESSENTA = np.pi/3

if __name__ == '__main__':
    print("Exercício 1")
    p = Point(2, 0)
    q = Point(4, 0)
    p.rotate(SESSENTA)
    q.rotate(SESSENTA)
    print("P: %.2f %.2f" % (p.x, p.y))
    print("Q: %.2f %.2f\n" % (q.x, q.y))

    print("Exercício 2")
    p = Point(2, 0)
    q = Point(4, 0)
    p.reverse_translation(2, 0)
    q.reverse_translation(2, 0)
    p.rotate(SESSENTA)
    q.rotate(SESSENTA)
    p.translation(2, 0)
    q.translation(2, 0)
    print("P: %.2f %.2f" % (p.x, p.y))
    print("Q: %.2f %.2f\n" % (q.x, q.y))

    print("Exercício 3")
    p = Point(2, 0)
    q = Point(4, 0)
    p.reverse_translation(3, 0)
    q.reverse_translation(3, 0)
    p.rotate(SESSENTA)
    q.rotate(SESSENTA)
    p.translation(3, 0)
    q.translation(3, 0)
    print("P: %.2f %.2f" % (p.x, p.y))
    print("Q: %.2f %.2f\n" % (q.x, q.y))
