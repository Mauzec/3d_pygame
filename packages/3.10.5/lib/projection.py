from math import tan
from numpy import array

class Projection:
    def __init__(self, render):
        right = tan(render.camera.hfov / 2)
        top = tan(render.camera.vfov / 2)
        
        near = render.camera.near_plane
        far = render.camera.far_plane
        
        left, bottom = -right, -top
        
        a = 2 / (right - left)
        b = 2 / (top - bottom)
        c = (far + near) / (far - near)
        d = 2 * near * far / (near - far)
        
        self.projection_matrix = array([
            [a,0,0,0],
            [0,b,0,0],
            [0,0,c,1],
            [0,0,d,0]
        ])
        
        w, h = render.width // 2, render.height // 2
        self.toscreen_matrix = array([
            [w,0,0,0],
            [0, -h,0,0],
            [0,0,1,0],
            [w, h, 0, 1]
        ])