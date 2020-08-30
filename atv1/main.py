import argparse
import cv2 as cv
import numpy as np


def normalize(r, g, b):
    return (r/255., g/255., b/255.)


def rgb2cmyk(r_, g_, b_):
    r, g, b = normalize(r_, g_, b_)

    c = 1 - r
    m = 1 - g
    y = 1 - b

    k = min(c, m, y)
    c = (c - k)/(1-k)
    m = (m - k)/(1-k)
    y = (y - k)/(1-k)

    c = c + k
    m = m + k
    y = y + k
    return (c, m, y, k)


def rgb2hsi(r_, g_, b_):
    r, g, b = normalize(r_, g_, b_)

    num = 0.5 * ((r - g) + (r - b))
    den = np.sqrt((r - g)**2 + (r-b)*(g-b))
    thetha = float(np.arccos(num/den))

    if b <= g:
        h = thetha
    elif b > g:
        h = 2*np.pi - thetha

    minRGB = min(r, g, b)
    rgb_sum = r + g + b
    s = 1 - 3 * minRGB/rgb_sum

    i = rgb_sum/3.

    return (h, s, i)


# TO RUN: $ python main.py -i <image path>
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", required=True,
                    help="path to input image")
    args = vars(ap.parse_args())
    img = cv.imread(args["i"])
    cv.imshow('img', img)

    b, g, r = cv.split(img)
    height, width = b.shape

    ####################### RGB2CMYK #######################

    c = np.zeros((height, width))
    m = np.zeros((height, width))
    y = np.zeros((height, width))
    k = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            c[i][j], m[i][j], y[i][j], k[i][j] = rgb2cmyk(
                r[i][j], g[i][j], b[i][j])

    cmyk = cv.merge((c, m, y, k))
    cv.imshow('cmyk', cmyk)
    # cv.imshow('c', c)
    # cv.imshow('m', m)
    # cv.imshow('y', y)

####################### ####################### #######################

    ####################### RGB2HSI #######################

    h = np.zeros((height, width))
    s = np.zeros((height, width))
    i = np.zeros((height, width))

    for k in range(height):
        for j in range(width):
            h[k][j], s[k][j], i[k][j] = rgb2hsi(r[k][j], g[k][j], b[k][j])

    hsi = cv.merge((h, s, i))
    cv.imshow('hsi', hsi)
    # cv.imshow('h', h)
    # cv.imshow('s', s)
    # cv.imshow('i', i)

####################### ####################### #######################
    k = cv.waitKey(0) & 0xFF
    if k == 27 or k == ord('q'):
        cv.destroyAllWindows()
