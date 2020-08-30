import numpy as np
import cv2 as cv
import sys
import os


def normalize(matrix):
    return matrix/255.


def showImg(title, img):
    cv.imshow(title, img)
    k = cv.waitKey(0) & 0xFF
    if k == 27 or k == ord('q'):
        cv.destroyAllWindows()


def cosDCT(x, u, N):
    return np.cos(((2.*x+1)*u*np.pi)/(2*N))


def alfa(u, N):
    if u == 0:
        return np.sqrt(1./N)
    elif u > 0:
        return np.sqrt(2./N)


def f(img, u, v):
    s = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            s += img[x, y] * cosDCT(x, u, img.shape[0]) * \
                cosDCT(y, v, img.shape[1])
    return s


def lowPass(img, radius):
    print("Calculando filtro passsa baixa...")
    r = np.zeros((img.shape))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.sqrt(i**2+j**2) > radius:
                r[i, j] = 0
            else:
                r[i, j] = img[i, j]
    return r


def highPass(img, radius):
    print("Calculando filtro passsa alta...")
    r = np.zeros((img.shape))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if np.sqrt(i**2+j**2) <= radius:
                r[i, j] = 0
            else:
                r[i, j] = img[i, j]
    return r


def dct(img):
    print("Calculando transformada do cosseno...")
    c = np.zeros((img.shape))
    for u in range(c.shape[0]):
        print(u)
        for v in range(c.shape[1]):
            au = alfa(u, c.shape[0])
            av = alfa(v, c.shape[1])
            s = f(img, u, v)
            c[u, v] = au*av*s
    return c


def idct(img):
    print("Calculando transformada inversa do cosseno...")
    f = np.zeros((img.shape))
    for x in range(f.shape[0]):
        print(x)
        for y in range(f.shape[1]):
            s = 0
            for u in range(img.shape[0]):
                for v in range(img.shape[1]):
                    au = alfa(u, img.shape[0])
                    av = alfa(v, img.shape[1])
                    s += au * av * img[u, v]*cosDCT(x, u, img.shape[0]) * \
                        cosDCT(y, v, img.shape[1])
            f[x, y] = s
    return f


if __name__ == '__main__':
    img = cv.imread('lena.jpg', 0)
    resize = 50
    img = cv.resize(img, (resize, resize))
    dct = dct(img)
    cv.imwrite('dct.jpg', dct)

    low = lowPass(dct, 20)
    cv.imwrite('low.jpg', low)

    high = highPass(dct, 20)
    cv.imwrite('high.jpg', high)

    low_idct = idct(low)
    cv.imwrite('low-idct.jpg', low_idct)

    high_idct = idct(high)
    cv.imwrite('high-idct.jpg', high_idct)

    noise = cv.imread('noise-freq.jpg')
    nl = lowPass(noise, 20)
    nh = highPass(noise, 20)
    noise_low_idct = idct(nl)
    noise_high_idct = idct(nh)
    cv.imwrite('noise-low-idct.jpg', noise_low_idct)
    cv.imwrite('noise-high-idct.jpg', noise_high_idct)

    # # dct = normalize(dct)
    # # showImg('discret-cos-transform' + str(resize), dct)
    # low = normalize(low)
    # showImg('low', low)
    # high = normalize(high)
    # showImg('high', high)
    # low_idct = normalize(low_idct)
    # showImg('low_idct.jpg', low_idct)
    # high_idct = normalize(high_idct)
    # showImg('high_idct.jpg', high_idct)
