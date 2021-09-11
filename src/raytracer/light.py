from dataclasses import dataclass
from . import Point
from . import Colour

@dataclass
class Light:
	position: Point
	colour: Colour