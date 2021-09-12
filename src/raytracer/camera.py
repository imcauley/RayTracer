from dataclasses import dataclass
import numpy as np
from raytracer import Point, Ray

@dataclass
class Camera:
    width: int
    height: int

    position: Point
    direction: Point

    height_fov: float = 1.5707963268
    width_fov: float = 1.5707963268

    def create_rays(self):
        width_step = self.width / self.width_fov
        height_step = self.height / self.height_fov
        
        start = self.direction.copy()
        start.translate(self.position)
        start.y_rotation(-self.height_fov / 2)
        start.x_rotation(-self.width_fov / 2)
        
        rays = []
        
        for i in range(0, self.height):
            row_start = start.copy()
            row_start.y_rotation(i * height_step)
            
            for j in range(0, self.width):
                current = row_start.copy()
                current.x_rotation(j * width_step)
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

        return brightnesses