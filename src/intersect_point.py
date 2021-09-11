from point import Point
from object import Object
from ray import Ray
from dataclasses import dataclass

@dataclass
class IntersectPoint:
    point: Point
    reflection: Ray
    distance: float
    intersecting_object: Object