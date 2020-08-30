import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

LMAX = 256


def calcHist(img):
    h, w = img.shape
    hist = np.zeros((LMAX))
    for i in range(h):
        for j in range(w):
            hist[img[i, j]] += 1
    return hist


def calcProb(hist, totalPix):
    prob = np.zeros((LMAX))
    for i in range(hist.size):
        prob[i] = hist[i]/totalPix
    return prob


def probClass(hist, T):
    c1 = c2 = 0
    for i in range(T):
        c1 += hist[i]
    c2 = 1 - c1
    return (c1, c2)


def mediaItensity(hist, T, pc1, pc2):
    s1 = s2 = 0
    for i in range(T):
        s1 += i*hist[i]
    m1 = s1/pc1
    for i in range(T, LMAX):
        s2 += i*hist[i]
    m2 = s2/pc2
    mg = s1 + s2
    return (mg, m1, m2)


def showHist(hist):
    plt.xlim([-0.5, 255.5])
    plt.plot(hist)
    plt.show()


def applyT(img, T):
    result = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i, j] <= T):
                result[i, j] = 0
            elif(img[i, j] > T):
                result[i, j] = 255
    return result


def showImg(title, img):
    cv.imshow(title, img)
    k = cv.waitKey(0) & 0xFF
    if k == 27 or k == ord('q'):
        cv.destroyAllWindows()


if __name__ == '__main__':
    img = cv.imread('lena.jpg', 0)
    hist = calcHist(img)
    probHist = calcProb(hist, img.shape[0] * img.shape[1])
    # showHist(probHist)
    v = 0
    for t in range(1, LMAX-1):
        prob_c1, prob_c2 = probClass(probHist, t)
        global_media, media_c1, media_c2 = mediaItensity(
            probHist, t, prob_c1, prob_c2)
        variance = (prob_c1*(media_c1 - global_media)**2) + \
            (prob_c2*(media_c2 - global_media)**2)
        if variance > v:
            v = variance
            T = t
    # print(T)
    r = applyT(img, T)
    showImg('threshold-image', r)
    cv.imwrite('threshold-img.jpg', r)
