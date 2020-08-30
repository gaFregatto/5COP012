import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translation(self, deltaX, deltaY):
        m = np.array([[1, 0, deltaX], [0, 1, deltaY], [0, 0, 1]])
        p = np.array([[self.x], [self.y], [1]])
        res = np.dot(m, p)
        self.x = res[0, 0]
        self.y = res[1, 0]

    def scale(self, lambdaX, lambdaY):
        m = np.array([[lambdaX, 0, 0], [0, lambdaY, 0], [0, 0, 1]])
        p = np.array([[self.x], [self.y], [1]])
        res = np.dot(m, p)
        self.x = res[0, 0]
        self.y = res[1, 0]

    def rotate(self, degree):
        m = np.array([[np.cos(degree), -np.sin(degree), 0],
                      [np.sin(degree), np.cos(degree), 0],
                      [0, 0, 1]])
        p = np.array([[self.x], [self.y], [1]])
        res = np.dot(m, p)
        self.x = res[0, 0]
        self.y = res[1, 0]

    def reverse_translation(self, deltaX, deltaY):
        m = np.array([[1, 0, -deltaX], [0, 1, -deltaY], [0, 0, 1]])
        p = np.array([[self.x], [self.y], [1]])
        res = np.dot(m, p)
        self.x = res[0, 0]
        self.y = res[1, 0]

    def reverse_scale(self, lambdaX, lambdaY):
        m, = np.array([[1/lambdaX, 0, 0], [0, 1/lambdaY, 0], [0, 0, 1]])
        p = np.array([[self.x], [self.y], [1]])
        res = np.dot(m, p)
        self.x = res[0, 0]
        self.y = res[1, 0]

    def reverse_rotate(self, degree):
        m = np.array([[np.cos(degree), np.sin(degree), 0],
                      [-np.sin(degree), np.cos(degree), 0],
                      [0, 0, 1]])
        p = np.array([[self.x], [self.y], [1]])
        res = np.dot(m, p)
        self.x = res[0, 0]
        self.y = res[1, 0]

    def show(self):
        print(self.x, self.y)
