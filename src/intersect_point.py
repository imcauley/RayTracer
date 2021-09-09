from point import Point
from dataclasses import dataclass

@dataclass
class IntersectPoint:
    point: Point
    reflection_direction: Point
    distance: float