from raytracer import Object, Point, Ray
import numpy as np
import math

class Plane(Object):
    def __init__(self, position, colour, normal):
        super().__init__(position, colour)
        self.normal = normal

    def intersect(self, ray: Ray):
        will_hit = np.dot(ray.vector(), self.normal)
        if(will_hit > 0.95):
            return None

        t = np.dot(np.subtract(ray.origin.vector, self.position), self.normal) / np.dot(self.normal, ray.direction.vector)

        return self.create_intersect_point(ray, t)

    def normal_at_point(self, point: Point) -> Point:
        return Point(self.normal)