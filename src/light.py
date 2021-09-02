from dataclasses import dataclass
from point import Point
from colour import Colour

@dataclass
class Light:
	position: Point
	colour: Colour