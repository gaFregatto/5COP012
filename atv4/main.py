import numpy as np
import cv2 as cv
import sys
import os


def showImg(img):
    cv.imshow('img', img)
    k = cv.waitKey(0) & 0xFF
    if k == 27 or k == ord('q'):
        cv.destroyAllWindows()


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
                    res[i][j][k] = abs(np.sum(aux))
    return res


def laplacianFilter(img):
    print('Calculando filtro Laplaciano...')
    mask = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    res = convolution(img, mask)
    # showImg(res)
    return res


def sobelFilter(img):
    print('Calculando filtro Sobel...')
    maskH = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    maskV = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobelX = convolution(img, maskH)
    sobelY = convolution(img, maskV)
    sobel = (sobelX + sobelY)/2
    sobel = np.uint8(sobel)
    # showImg(sobelX)
    # showImg(sobelY)
    # showImg(sobel)
    return sobel


if __name__ == '__main__':
    img = cv.imread('lena.jpg')
    lpc = laplacianFilter(img)
    sbl = sobelFilter(img)
    cv.imwrite('laplacian3.png', lpc)
    cv.imwrite('sobel3.png', sbl)
