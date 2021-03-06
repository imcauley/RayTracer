import raytracer as rt
import numpy as np

if __name__ == '__main__':
    s = rt.Sphere(np.array([0, 3, 0], 'f'), np.array([0.5, 0.5, 0], 'f'), 1)
    l = rt.Light(
        rt.Point(np.array([0.6, 0.6, 0], 'f')), 
        rt.Colour(np.array([1,1,1], 'f'))
        )
    c = rt.Camera(
        800, 
        800, 
        rt.Point(np.array([0, 0, 0], 'f')), 
        rt.Point(np.array([0, 1, 0], 'f'))
        )
    
    c.create_rays()
    c.create_image([s], [l])