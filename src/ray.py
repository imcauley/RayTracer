import numpy as np

class Ray:
    def __init__(self, origin, direction, time_to_live=5):
        self.origin = origin
        self.direction = direction
        self.time_to_live = time_to_live

    def vector(self):
        return self.direction - self.origin

    def colour_from_ray(self, objects, lights):
        intersecting_point = self.intercepting_point(objects)

        if intersecting_point is None:
            return None
        
        brightness = 0
        for light in lights:
            brightness += np.dot(light.origin, intersecting_point.reflection.vector())

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