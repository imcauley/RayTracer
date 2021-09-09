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
            return self.create_intersect_point(ray, t)

        n = -b + math.sqrt(d)
        if n  > 0:
            t = n / (2 * a)
            return self.create_intersect_point(ray, t)

        return None

    def normal_at_point(self, point: Point) -> Point:
        return Point(point.vector - self.position)