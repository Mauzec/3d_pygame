import math
import pygame as pg
from matrix import *
from math import pi


class Camera:
    def __init__(self, render, x,y,z):
        self.render = render
        self.pos = np.array([x,y,z,1])
        
        self.right = np.array([1,0,0,1])
        self.forward = np.array([0,0,1,1])
        self.up = np.array([0,1,0,1])
        
        self.hfov = pi /2
        self.vfov = self.hfov * (render.height / render.width)
        
        self.near_plane = 0.1
        self.far_plane = 100
        
        self.movespeed = 0.1
        self.rotatespeed = 0.02
        
    def translate_matrix(self):
        x,y,z,w = self.pos
        return np.array([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [-x,-y,-z,1]
        ])
        
    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
    
    def matrix(self):
        return self.rotate_matrix() @ self.translate_matrix()
    
    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.pos -= self.right * self.movespeed
        if key[pg.K_d]:
            self.pos += self.right * self.movespeed
        if key[pg.K_w]:
            self.pos += self.forward * self.movespeed
        if key[pg.K_s]:
            self.pos -= self.forward * self.movespeed
        if key[pg.K_q]:
            self.pos += self.up * self.movespeed
        if key[pg.K_z]:
            self.pos -= self.up * self.movespeed
        
        
        # if [event for event in pg.event.get() if event.type == pg.MOUSEBUTTONUP or event.type == pg.MOUSEBUTTONDOWN]:
        #     ox, oy = pg.mouse.get_pos()
        #     while pg.mouse.get_pressed()[0]:
        #         x, y = pg.mouse.get_pos()
        #         x, y = x - ox, y - ox
        #         print(x,y)
        #         if x > 0:
        #             self.forward = self.forward @ y_rotate_matrix(self.rotatespeed)
                
        #         old = pg.mouse.get_pos()