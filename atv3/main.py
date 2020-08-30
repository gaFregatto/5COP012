import sys
import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def convolution(img, mask):
    res = np.ones((img.shape), np.uint8)
    (width, height) = mask.shape

    i_offset = width/2 - .5
    j_offset = height/2 - .5

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            xi = int(i-i_offset)
            xf = int(i+i_offset)
            yi = int(j-j_offset)
            yf = int(j+j_offset)

            for k in range(img.shape[2]):
                if(xi < 0 or yi < 0 or xf >= img.shape[0] or yf >= img.shape[1]):
                    res[i][j][k] = 0
                else:
                    aux = np.zeros((mask.shape))
                    aux = (img[xi:xf+1, yi:yf+1, k] * mask)
                    res[i][j][k] = np.sum(aux)/np.sum(mask)
    return res


def showImg(img):
    cv.imshow('img', img)
    k = cv.waitKey(0) & 0xFF
    if k == 27 or k == ord('q'):
        cv.destroyAllWindows()


def mediumFilter(img, n_mask):
    print('Calculando filtro da média...')
    mask = np.ones((n_mask, n_mask))
    res = convolution(img, mask)
    # showImg(res)
    return res


def weightedAverageFilter(img, n_mask):
    print('Calculando filtro da média ponderada...')

    if n_mask == 3:
        mask = np.array(([1, 2, 1], [2, 4, 2], [1, 2, 1]))
    elif n_mask == 5:
        mask = np.array(([1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [
                         7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]))

    res = convolution(img, mask)
    # showImg(res)
    return res


if __name__ == '__main__':
    img = cv.imread('sky.png')
    medium = mediumFilter(img, 7)
    weighted = weightedAverageFilter(img, 5)
    cv.imwrite('medium7.png', medium)
    cv.imwrite('weighted5.png', weighted)
