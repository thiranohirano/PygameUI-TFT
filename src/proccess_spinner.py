'''
Created on 2016/03/02

@author: hirano
'''
from string import maketrans

import pygame, time
import mycolors
from pygameui.colors import black_color, white_color
import threading
class ProccessSpinner():
    '''
    classdocs
    '''
    def __init__(self, screen, title=''):
        self.size = 100
        self.current_frame = 0
        self.frame_count = 32
        self.spinnering_flag = True
        self.screen = screen
        self.rect = self.screen.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height

        pygame.font.init() # Just in case 
        self.titleFont = pygame.font.SysFont('Courier New', 24, bold=True) # keyboard font
        # make a copy of the screen
        self.screenCopy = screen.copy()
        # create a background surface
        self.background = pygame.Surface(self.rect.size)
        self.background.fill((0,0,0)) # fill with black
        self.background.set_alpha(191) # 50% transparent
        # blit background to screen
        self.screen.blit(self.background,(0,0))
        
        text = self.titleFont.render(title, 1, white_color)
        textpos = text.get_rect()
        blockoffx = (self.w / 2)
        blockoffy = (self.h / 2)
        offsetx = blockoffx - (textpos.width / 2)
        offsety = blockoffy - textpos.height - self.size / 2 - 20
        screen.blit(text, (offsetx,offsety))
        pygame.display.update()
        
    def run(self, slot):
        t = threading.Thread(target=self.spinnering)
        t.start()
        slot()
        self.spinnering_flag = False
        t.join()
        self.clear()
        
    def spinnering(self):
        while self.spinnering_flag:
            time.sleep(0.05)
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.draw(self.screen, self.background)
            
    def draw(self, screen, background):
        center_x = self.size /2
        center_y = self.size /2
        frame_pattern = self.current_frame / 8
        layer = pygame.Surface((self.size,self.size))
        layer.set_colorkey(black_color)
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
        layer.set_alpha(255 - (((self.current_frame % 8) + 1) * 32))
        layer2.set_alpha(192)
        screen_center_x = (self.w - self.size) / 2
        screen_center_y = (self.h - self.size) / 2
        screen.blit(background, (screen_center_x,screen_center_y), (screen_center_x,screen_center_y, self.size, self.size))
        screen.blit(layer, (screen_center_x, screen_center_y))
        screen.blit(layer2, (screen_center_x,screen_center_y))
        pygame.display.update()
        
    def clear(self):    
        ''' Put the screen back to before we started '''
        self.screen.blit(self.screenCopy,(0,0))
        pygame.display.update()