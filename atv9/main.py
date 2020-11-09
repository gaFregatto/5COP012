from Point import *
import cv2 as cv 
def bresenham(p1, p2):
    res = []
    p = 2 * (p2.y - p1.y)
    p_error = p - (p2.x - p1.x)

    y = p1.y
    for x in range(p1.x, p2.x+1):
        # print(f"({x},{y})")
        res.append((x, y))
        p_error += p 
        if p_error >= 0:
            y += 1
            p_error += - 2 * (p2.x - p1.x) 
    return res
        

if __name__ == '__main__':
    p1 = Point(3, 2)
    p2 = Point(15, 5)
    line = bresenham(p1, p2)
    print(f"PONTOS QUE DEFINEM A RETA: {line}")
 