import pygame as pg
from matrix import *


class get_rotate_n:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args):
        if len(args) > 2:
            return self.func(*args)
        axis = args[0]
        if axis == 'x':
            return self.func(*args, x_rotate_matrix)
        if axis == 'y':
            return self.func(*args, y_rotate_matrix)
        if axis == 'z':
            return self.func(*args, z_rotate_matrix)
        
        return self.func(*args)


class Object:
    def __init__(self, render) -> None:
        self.render = render
        self.vertexes = np.array([[0,0,0,1], [0,1,0,1], [1,1,0,1], [1,0,0,1], 
                                   [0,0,1,1], [0,1,1,1], [1,1,1,1], [1,0,1,1]])
        self.faces = np.array([[0,1,2,3], [4,5,6,7], 
                      [0,4,5,1], [2,3,7,6],
                      [1,2,6,5], [0,3,7,4]])
        
    def translate(self, *args):
        self.vertexes = self.vertexes @ translate_matrix(*args)
    
    def scale(self, *args):
        self.vertexes = self.vertexes @ scale_matrix(*args)
        
    @get_rotate_n
    def rotate(axis, angle, func=None):
        if not func: raise AttributeError(f'Wrong attribute axis: {axis}')
        return func(angle)
    
    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ y_rotate_matrix(angle)