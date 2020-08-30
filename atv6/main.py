import numpy as np
import cv2 as cv
import sys
import os

from Point import *
TRINTA = np.pi/6
QC = np.pi/4
SESSENTA = np.pi/3

if __name__ == '__main__':
    print("PONTO P: um de cada vez")
    p = Point(1, 1)
    p.translation(-1, 0)
    p.scale(1, 2)
    p.rotate(QC)
    p.show()
    print("PONTO P: boss")
    pp = Point(1, 1)
    pp.boss(-1, 0, 1, 2, QC)
    pp.show()

    print("PONTO Q: um de cada vez")
    q = Point(3, 7)
    q.translation(-1, 0)
    q.scale(1, 2)
    q.rotate(QC)
    q.show()
    print("PONTO Q: boss")
    qq = Point(3, 7)
    qq.boss(-1, 0, 1, 2, QC)
    qq.show()
