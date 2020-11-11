from Point import *


class Sphere:
    def __init__(self, center, r):
        self.center = center
        self.radius = r

    def __repr__(self):
        return f"Sephere(center:({self.center}), radius:{self.radius})"
