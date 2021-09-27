import numpy as np
from raytracer import Point

class Ray:
    def __init__(self, origin: Point, direction: Point, time_to_live=5):
        self.origin = origin
        self.direction = direction
        self.time_to_live = time_to_live

    def __str__(self) -> str:
        return str(self.origin.vector) + ' -> ' + str(self.direction.vector)

    def vector(self):
        return np.subtract(self.direction.vector, self.origin.vector)

    def normalize(self):
        norm_direction = self.vector()
        norm_direction = norm_direction / np.linalg.norm(norm_direction)
        norm_direction = norm_direction + self.origin.vector
        self.direction = Point(norm_direction)

    def colour_from_ray(self, objects, lights):
        intersecting_point = self.intercepting_point(objects)
        if intersecting_point is None:
            return np.array([0,0,0], 'f')

        brightness = 0
        for light in lights:
            similarity =  np.dot(light.position.vector, intersecting_point.reflection.vector())
            brightness += abs(similarity)

        return intersecting_point.intersecting_object.colour * brightness

    def intercepting_point(self, objects):
        intersect_point = None
        
        for obj in objects:
            if point := obj.intersect(self):
                if intersect_point is None:
                    intersect_point = point
                else:
                    if point.distance < intersect_point.distance:
                        intersect_point = point

        return intersect_point