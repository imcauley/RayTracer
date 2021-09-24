import unittest
import sys
sys.path.append('./src')

from raytracer import Ray
from raytracer import Point
import math

import numpy as np

class TestIntersects(unittest.TestCase):
    def test_x_rotation(self):
        p = Point(np.array([2, 0, 0], dtype='f'))
        p.y_rotation(math.pi)

        self.assertAlmostEqual(p.vector[0], -2)
        self.assertAlmostEqual(p.vector[1], 0)
        self.assertAlmostEqual(p.vector[2], 0)

    def test_y_rotation(self):
        p = Point(np.array([0, 2, 0], dtype='f'))
        p.y_rotation(math.pi)

        self.assertAlmostEqual(p.vector[0], 0)
        self.assertAlmostEqual(p.vector[1], -2)
        self.assertAlmostEqual(p.vector[2], 0)

    def test_z_rotation(self):
        p = Point(np.array([0, 0, 2], dtype='f'))
        p.z_rotation(math.pi)

        self.assertAlmostEqual(p.vector[0], 0)
        self.assertAlmostEqual(p.vector[1], 0)
        self.assertAlmostEqual(p.vector[2], -2)

    def test_half_rotation(self):
        p = Point(np.array([1, 0, 0], dtype='f'))
        p.z_rotation(math.pi/2)

        self.assertAlmostEqual(p.vector[0], 0)
        self.assertAlmostEqual(p.vector[2], -1)

    def test_quater_rotation(self):
        p = Point(np.array([1, 0, 0], dtype='f'))
        p.z_rotation(math.pi/4)

        self.assertAlmostEqual(p.vector[0], 0.70710678)
        self.assertAlmostEqual(p.vector[2], -0.70710678)

if __name__ == '__main__':
    unittest.main()