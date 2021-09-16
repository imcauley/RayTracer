import unittest
import sys
sys.path.append('./src')

from raytracer import Ray
from raytracer import Point
import math

import numpy as np

class TestIntersects(unittest.TestCase):
    def test_z_rotation(self):
        p = Point(np.array([0, 1, 0], dtype='f'))
        p.z_rotation(math.pi)

        self.assertAlmostEqual(p.vector[1], -1)

if __name__ == '__main__':
    unittest.main()