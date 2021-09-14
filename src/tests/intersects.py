import unittest
import sys
sys.path.append('./src')

from raytracer import Sphere
from raytracer import Ray
from raytracer import Point

import numpy as np

class TestIntersects(unittest.TestCase):
    def test_sphere_hit(self):
        r = Ray(
            Point(np.array([0, 0, 0], dtype='f')), 
            Point(np.array([0, 1, 0], dtype='f'))
            )
        s = Sphere(
            np.array([0, 3, 0], dtype='f'), 
            np.array([0.5, 0.5, 0], dtype='f'), 
            1
            )

        self.assertIsNotNone(s.intersect(r))

    def test_sphere_miss(self):
        r = Ray(
            Point(np.array([0, 0, 0], dtype='f')), 
            Point(np.array([0, -1, 0], dtype='f'))
            )
        s = Sphere(
            np.array([0, 3, 0], dtype='f'), 
            np.array([0.5, 0.5, 0], dtype='f'), 
            1
            )

        i = s.intersect(r)
        self.assertIsNone(i)

if __name__ == '__main__':
    unittest.main()