from raytracer import Object, Point, Ray
import numpy as np
import math

class Plane(Object):
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, colour):
        position = (point_a.vector + point_b.vector + point_c.vector) / 3.0
        super().__init__(position, colour)
        self.a = point_a
        self.b = point_b
        self.c = point_c

    def intersect(self, ray: Ray):
        will_hit = np.dot(ray.vector(), self.normal)
        if(will_hit > 0.95):
            return None

        t = np.dot(np.subtract(ray.origin.vector, self.position), self.normal) / np.dot(self.normal, ray.direction.vector)

        return self.create_intersect_point(ray, t)

    def normal_at_point(self, point: Point) -> Point:
        ab = np.subtract(self.b, self.a)
        ac = np.subtract(self.c, self.a)
        normal = np.cross(ab, ac)
        return Point(normal)