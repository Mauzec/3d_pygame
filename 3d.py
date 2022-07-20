from locale import normalize
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath('__file__')) + '/packages/3.10.5/lib')

import pygame as pg

from object import *
from camera import *
from projection import *

class Render:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 1280, 720
        self.fps = 60
        
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        
        self.create_camera()  
        self.create_projection() 
        self.create_object()      
    
    def create_object(self):
        self.object = Object(self)
        self.object.rotate_y(pi/6)
        self.object.translate(-2, 2, -25)

    def create_projection(self):
        self.projection = Projection(self)
    
    def scr_project_pos(self):
        a = self.object.vertexes @ self.camera.matrix()
        a = a @ self.projection.projection_matrix
        a /= a[:, -1].reshape(-1, 1)
        a[(a > 2) | (a < -2)] = 0
        a = a @ self.projection.toscreen_matrix
        a = a[:, :2]
        return a
    
    def draw(self, back):
        self.screen.fill(pg.Color(back))
        vertexes = self.scr_project_pos()
        for face in self.object.faces:
            polygon = vertexes[face]
            pg.draw.polygon(self.screen, pg.Color('orange'), polygon, 3)
        return vertexes
            
    def create_camera(self):
        self.camera = Camera(self, 0.5,1,-55)
    
    def run(self):
        while 1:
            [exit() for event in pg.event.get() if event.type == pg.QUIT]
            for a,b in enumerate(self.draw('gray')):
                b = pg.font.SysFont('Times New Roman', 14).render(f'{b}', False, (255,255,255))
                self.screen.blit(b, (1000, a*30))
            
            self.camera.control()
            
            a = pg.font.SysFont('Times New Roman', 30).render(f'{self.camera.pos[0]}', False, (255,255,255))
            b = pg.font.SysFont('Times New Roman', 30).render(f'{self.camera.pos[1]}', False, (255,255,255))
            c = pg.font.SysFont('Times New Roman', 30).render(f'{self.camera.pos[2]}', False, (255,255,255))
            self.screen.blit(a, (0,0))
            self.screen.blit(b, (0, 40))
            self.screen.blit(c, (0, 80))
            
            pg.display.set_caption(str(self.clock.get_fps()))     
            pg.display.flip()  
            self.clock.tick(self.fps)
            

if __name__ == '__main__':
    soft = Render()
    soft.run()