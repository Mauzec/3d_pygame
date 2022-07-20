from math import cos, sin
import numpy as np

def translate_matrix(dx,dy,dz):
    return np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [dx,dy,dz,1]
    ])

def scale_matrix(sx,sy,sz):
    return np.array([
        [sx,0,0,1],
        [0,sy,0,1],
        [0,0,sz,0],
        [0,0,0,1]
    ])

def x_rotate_matrix(angle):
    return np.array([
        [1,0,0,0],
        [0,cos(angle), sin(angle), 0],
        [0, -sin(angle), cos(angle), 0],
        [0,0,0,1]
    ])
    
def y_rotate_matrix(angle):
    return np.array([
        [cos(angle), 0, -sin(angle), 0],
        [0,1,0,0],
        [sin(angle), 0, cos(angle),0],
        [0,0,0,1]
    ])
    
def z_rotate_matrix(angle):
    return np.array([
        [cos(angle), sin(angle), 0, 0],
        [-sin(angle), cos(angle), 0, 0],
        [0,0,1,0],
        [0,0,0,1]
    ])