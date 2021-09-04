from object import Object
from point import Point
import numpy as np
import math

class Sphere(Object):
    def __init__(self, position, radius):
        super().__init__(position)
        self.radius = radius

    def intersect(self, ray):
        a = np.dot(ray.direction, ray.direction)
        b = 2 * np.dot(ray.direction, ray.origin - self.position)
        c = (self.radius ** 2) * np.dot(ray.origin - self.position, ray.origin - self.position)

        d = (b ** 2) - (4 * a * c)

        if d < 0:
            return None

        t_plus = (b + math.sqrt(d)) / (2 * a)
        t_min = (b - math.sqrt(d)) / (2 * a)

        if t_plus < t_min and t_plus > 0:
            t = t_plus
        elif t_min > 0:
            t = t_min
        else:
            return None

        p = ray.origin + (t * ray.direction)
        return Point(p)