import numpy as np
import math

def createRay(camera, i, j):
    p0 = np.array(camera)
    p = np.array([i, j, 1])
    d = math.sqrt(sum(p**2))
    v = (p-p0)/d
    return np.array([p0, v])

def findIntersection(ray, sphere):
    p0 = np.array(ray[0])
    v = np.array(ray[1])

    C = np.array(sphere[0])
    result = [] 
    r = sphere[1]

    aux = p0 - C

    a = 1
    b = np.matmul(2*v, aux)
    c = np.matmul(aux, aux) - r**2
    
    delta = b**2 - 4 * a * c 
    t1 = (-b + math.sqrt(delta))/2*a
    t2 = (-b - math.sqrt(delta))/2*a
    
    t = min(t1, t2)
    if t < 0:
        # intersection doesnt occur
        pass
    else:
        if t1 > 1:
            result.append(p0 + t1*v)
        if t2 > 1:
            result.append(p0 + t2*v)

    return result


if __name__ == "__main__":
    observer = [0, 0, 0]
    ray = createRay(observer, 1, 1)
    sphere = [[1.5, 1.5, 6], 4]
    intersections = findIntersection(ray, sphere)
    if len(intersections) == 2:
        print(f"(P:{intersections[1]}, P':{intersections[0]})")
    elif len(intersections) == 1:
        print(f"(P:{intersections[0]})")
    else:
        print("Nenhuma interseccao encontrada.")
    