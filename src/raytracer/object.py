from abc import ABC, abstractmethod
import numpy as np

from raytracer import Point, Ray, IntersectPoint

class Object(ABC):
    def __init__(self, position):
        self.position = position
        
    @abstractmethod
    def intersect(self, ray: Ray):
        pass

    @abstractmethod
    def normal_at_point(self, point: Point) -> Point:
        pass

    def reflection(self, ray: Ray, intercept_point: Point) -> Ray:
        d = ray.direction - ray.origin
        n = self.normal_at_point(intercept_point)

        r = d - (2 * (np.dot(d, n)) * n)
        r = r + intercept_point.vector

        return Ray(intercept_point, r, ray.time_to_live - 1)

    def create_intersect_point(self, ray, distance) -> IntersectPoint:
        point = ray.origin + (distance * ray.direction)
        reflection = self.reflection(ray, point)

        return IntersectPoint(point, reflection, distance, self)