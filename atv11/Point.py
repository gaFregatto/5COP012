class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x:{self.x}, y:{self.y})"

    def __sub__(a, b):
        return Point(a.x - b.x, a.y - b.y)
