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

    def unit_vector(self):
        v = np.subtract(self.direction.vector, self.origin.vector)
        return v / np.linalg.norm(v)

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
            if self.in_shadow(intersecting_point, light, objects):
                continue
            
            relative_light = np.subtract(light.position.vector, intersecting_point.point.vector)
            relative_light = relative_light / np.linalg.norm(relative_light)
            similarity =  np.dot(relative_light, intersecting_point.reflection.unit_vector())
            brightness += abs(similarity)

        if(brightness > 1):
            brightness = 1

        return intersecting_point.intersecting_object.colour * brightness

    def in_shadow(self, intersect_point, light, objects):
        BIAS = 0.1
        
        biased_point = intersect_point.point.vector + intersect_point.normal.vector * BIAS
        light_ray = Ray(Point(biased_point), light.position)
        return light_ray.has_intercept(objects)

    def has_intercept(self, objects) -> bool:
        for obj in objects:
            if obj.intersect(self):
                return True

        return False

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