from dataclasses import dataclass
from os import stat
import numpy as np
from raytracer import Point, Ray
from PIL import Image
import math

@dataclass
class Camera:
    width: int
    height: int

    position: Point
    direction: Point

    height_fov: float = math.pi * 90 / 180
    width_fov: float = 80

    def create_rays(self):
        aspect_ratio = self.width / self.height
        
        rays = []
        
        for i in range(0, self.height):            
            for j in range(0, self.width):
                Px = (2 * ((j + 0.5) / self.width) - 1) * np.tan(self.width_fov / 2 * math.pi / 180) * aspect_ratio
                Py = (1 - 2 * ((i + 0.5) / self.height) * np.tan(self.width_fov / 2 * math.pi / 180))
                
                direction = Point(np.array([Px, 1, Py]))
                r = Ray(self.position, direction)
                r.normalize()
                rays.append(r)
                
        self.rays = rays

    def create_image(self, objects, lights):
        row = 0
        col = 0
        brightnesses = np.zeros([self.width, self.height, 3], 'f')
        for ray in self.rays:
            b = ray.colour_from_ray(objects, lights)
            brightnesses[row, col] = b
            
            row += 1
            if row >= self.width:
                row = 0
                col += 0


        brightnesses = brightnesses * 255
        brightnesses = brightnesses.astype(np.uint8)

        img = Image.fromarray(brightnesses)
        img.show()
        # return brightnesses
