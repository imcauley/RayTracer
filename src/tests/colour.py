import unittest
import sys
sys.path.append('./src')

from raytracer import Sphere, Ray, Point, Light, Colour

import numpy as np

class TestIntersects(unittest.TestCase):
    def test_green_hit(self):
        r = Ray(
            Point(np.array([0, 0, 0], dtype='f')), 
            Point(np.array([0, 1, 0], dtype='f'))
            )
        s = Sphere(
            np.array([0, 3, 0], dtype='f'), 
            np.array([0, 1, 0], dtype='f'), 
            1
            )
        l = Light(
            Point(np.array([0, -1 , 0], 'f')), 
            Colour(np.array([1,1,1], 'f'))
            )

        c = r.colour_from_ray([s], [l])

        self.assertEqual(c, np.array([0, 1, 0]))

if __name__ == '__main__':
    unittest.main()