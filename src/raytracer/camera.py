from dataclasses import dataclass
from os import stat
import numpy as np
from raytracer import Point, Ray
from PIL import Image

@dataclass
class Camera:
    width: int
    height: int

    position: Point
    direction: Point

    height_fov: float = 1.5707963268
    width_fov: float = 1.5707963268

    def create_rays(self):
        width_step = self.width_fov / self.width
        height_step = self.height_fov / self.height
        
        start = self.direction.copy()
        start.translate(self.position)
        start.z_rotation(-self.height_fov / 2)
        start.x_rotation(-self.width_fov / 2)

        offset = Point(start.vector * -1.0)
        
        rays = []
        
        for i in range(0, self.height):            
            for j in range(0, self.width):
                current = start.copy()
                current.z_rotation(i * height_step)
                current.x_rotation(j * width_step)
                current.translate(offset)
                r = Ray(self.position, current)
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
