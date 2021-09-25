from . import Object
from . import Point
import numpy as np
import math

class Plane(Object):
    def __init__(self, position, colour, normal):
        super().__init__(position, colour)
        self.normal = normal