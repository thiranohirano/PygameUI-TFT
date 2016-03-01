'''
Created on 2016/03/01

@author: hirano
'''
import pygame
import pygame.gfxdraw
import myui as ui
import mycolors
from pygameui.colors import black_color

class MySpinner(ui.view.View):
    size = 100
    def __init__(self, frame, delay=1/10.0):
        self.size = MySpinner.size
        ui.view.View.__init__(self, ui.Rect(frame.x, frame.y, self.size, self.size))
        self.current_frame = 0
        self.elapsed = 0
        self.frame_count = 24
        self.delay = delay
        
    def update(self, dt):
        ui.view.View.update(self, dt)
        self.elapsed += dt
        if self.elapsed > self.delay:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.elapsed = 0
    def layout(self):
        self.current_frame = 0
        self.elapsed = 0
        ui.view.View.layout(self)
            
    def draw(self):
        if not ui.view.View.draw(self):
            return False
        
        center_x = self.size /2
        center_y = self.size /2
        frame_pattern = self.current_frame / 6
        layer = pygame.Surface((self.size,self.size))
        pygame.gfxdraw.filled_circle(layer, center_x,center_y, self.size / 2-5, mycolors.peter_river)
        pygame.gfxdraw.filled_circle(layer, center_x,center_y, self.size / 2 - 15, black_color)

        if frame_pattern == 0:
            pygame.gfxdraw.box(layer,  (center_x, center_y, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (0, 0, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (0, center_y, center_x, center_y), black_color)
        elif frame_pattern == 1:
            pygame.gfxdraw.box(layer,  (center_x, 0, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (0, 0, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (0, center_y, center_x, center_y), black_color)
        elif frame_pattern == 2:
            pygame.gfxdraw.box(layer,  (center_x, center_y, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (0, 0, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (center_x, 0, center_x, center_y), black_color)
        else:
            pygame.gfxdraw.box(layer,  (center_x, center_y, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (center_x, 0, center_x, center_y), black_color)
            pygame.gfxdraw.box(layer,  (0, center_y, center_x, center_y), black_color)
        layer2 = pygame.Surface((self.size,self.size))
        layer2.set_colorkey(black_color)
        pygame.gfxdraw.filled_circle(layer2, center_x, center_y, self.size / 2 -25, mycolors.peter_river)
        pygame.gfxdraw.filled_circle(layer2, center_x, center_y, self.size / 2 -30, black_color)
        layer.set_alpha(255 - (((self.current_frame % 6) + 1) * 32))
        layer2.set_alpha(192)
        self.surface.fill(black_color)
        self.surface.blit(layer, (0, 0))
        self.surface.blit(layer2, (0,0))