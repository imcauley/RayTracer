from object import Object
from point import Point
import numpy as np
import math

class Sphere(Object):
    def __init__(self, position, radius):
        super().__init__(position)
        self.radius = radius

    def intersect(self, ray):
        oc = ray.origin - self.position

        a = np.dot(ray.direction, ray.direction)
        b = 2 * np.dot(oc, ray.direction)
        c = np.dot(oc, oc) - (self.radius ** 2)

        d = (b ** 2) - (4 * a * c)

        if d < 0:
            return None

        n = -b - math.sqrt(d)
        if n > 0:
            t = n / (2*a)
            p = ray.origin + (t * ray.direction)
            return Point(p)

        n = -b + math.sqrt(d)
        if n  > 0:
            t = (-b - math.sqrt(d)) / (2 * a)
            p = ray.origin + (t * ray.direction)
            return Point(p)

        return None