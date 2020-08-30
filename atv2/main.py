import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

LMAX = 256


def calcHist(img):
    b, g, r = cv.split(img)
    h, w = b.shape
    hist = np.zeros((3, LMAX))
    for i in range(h):
        for j in range(w):
            hist[0][r[i][j]] += 1   # histR
            hist[1][g[i][j]] += 1   # histG
            hist[2][b[i][j]] += 1   # histB
    return hist


def normalizeHist(hist, totalPix):
    histNorm = np.zeros((3, LMAX))
    for i in range(histNorm.shape[0]):        # i percorre camadas
        for j in range(hist.shape[1]-1): 	    # j percorre vetores
            histNorm[i][j] = hist[i][j]/totalPix
    return histNorm


def calcHistAcc(hist):
    histAcc = np.zeros((3, LMAX))
    for i in range(hist.shape[0]):        # i percorre camadas
        histAcc[i][1] = hist[i][1]
        for j in range(hist.shape[1]-1):  # j percorre vetores
            histAcc[i][j+1] = histAcc[i][j] + hist[i][j+1]
    return histAcc


def equalizeImg(img, hist):
    result = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for k in range(img.shape[2]):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                result[i][j][k] = (LMAX - 1) * hist[2-k][img[i][j][k]]
    return result


def showHist(hist):
    colors = ['red', 'green', 'blue']
    for i in range(hist.shape[0]):
        plt.plot(hist[i], colors[i])
    plt.show()


if __name__ == '__main__':
    img = cv.imread('lena.jpg')
    hist = calcHist(img)
    histNorm = normalizeHist(hist, img.shape[0] * img.shape[1])
    histAcc = calcHistAcc(histNorm)
    showHist(histAcc)
    result = equalizeImg(img, histAcc)
    cv.imshow('result', result)
    # cv.imwrite('lena-norm.jpg', result)
    k = cv.waitKey(0) & 0xFF
    if k == 27 or k == ord('q'):
        cv.destroyAllWindows()
