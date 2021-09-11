from dataclasses import dataclass
from raytracer import Point

@dataclass
class Camera:
    width: int
    height: int

    position: Point
    direction: Point

    height_fov: float = 1.5707963268
    width_fov: float = 1.5707963268

    def create_rays(self):
        width_step = self.width / self.width_pov
        height_step = self.height / self.height_pov
        
        start = self.direction.copy()
        start.translate(self.position)
        start.rotate_y(-self.height_pov / 2)
        start.rotate_x(-self.width_pov / 2)
        
        rays = []
        
        for i in range(0, self.height):
            row_start = start.copy()
            row_start.rotate_y(i * height_step)
            
            for j in range(0, self.width):
                current = row_start.copy()
                current.rotate_x(j * width_step)
                rays.append(current)
                
                
        self.rays = rays

    def create_image(self, objects, lights):
        brightnesses = []
        for (index, ray) in enumerate(self.rays):
            b = ray.colour_from_ray(objects, lights)
            brightnesses.append(b)

        return brightnesses