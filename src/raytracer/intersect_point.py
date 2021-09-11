from dataclasses import dataclass
from typing import Any
from raytracer import Point, Ray

@dataclass
class IntersectPoint:
    point: Point
    reflection: Ray
    distance: float
    intersecting_object: Any