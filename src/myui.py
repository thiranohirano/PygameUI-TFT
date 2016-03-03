'''
Created on 2016/03/01

@author: hirano
'''
__version__ = '0.2.0'


import pygame

from pygameui.alert import *
from pygameui.button import *
from pygameui.callback import *
from pygameui.checkbox import *
from pygameui.dialog import *
from pygameui.flipbook import *
from pygameui.grid import *
from pygameui.imagebutton import *
from pygameui.imageview import *
from pygameui.label import *
from pygameui.listview import *
from pygameui.notification import *
from pygameui.progress import *
from pygameui.render import *
from pygameui.resource import *
from pygameui.scroll import *
from pygameui.select import *
from pygameui.slider import *
from pygameui.spinner import *
from pygameui.textfield import *
from pygameui.view import *

import pygameui.focus as focus
import pygameui.window as window
import pygameui.scene as scene
import pygameui.theme as theme

from pygameui.scene import Scene


import time


Rect = pygame.Rect
window_surface = None
ui_quit = False
event_flag = False

def init(name='', window_size=(640, 480)):
    pygame.init()
    pygame.key.set_repeat(200, 50)
    global window_surface
    window_surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption(name)
    window.rect = pygame.Rect((0, 0), window_size)
    theme.init()

def quit():
    global ui_quit
    ui_quit = True
    
def event_on():
    global event_flag
    event_flag = True

def run():
    global event_flag
    assert len(scene.stack) > 0

    clock = pygame.time.Clock()
    down_in_view = None

    elapsed = 0
    

    while True:
        time.sleep(0.01)
        dt = clock.tick(20)

        elapsed += dt
        if elapsed > 5000:
            elapsed = 0
#         event_flag = False
        events = pygame.event.get() 
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit()

            mousepoint = pygame.mouse.get_pos()

            if e.type == pygame.MOUSEBUTTONDOWN:
                hit_view = scene.current.hit(mousepoint)
                if (hit_view is not None and
                    not isinstance(hit_view, scene.Scene)):
                    focus.set(hit_view)
                    down_in_view = hit_view
                    pt = hit_view.from_window(mousepoint)
                    hit_view.mouse_down(e.button, pt)
                else:
                    focus.set(None)
                event_flag = True
            elif e.type == pygame.MOUSEBUTTONUP:
                hit_view = scene.current.hit(mousepoint)
                if hit_view is not None:
                    if down_in_view and hit_view != down_in_view:
                        down_in_view.blurred()
                        focus.set(None)
                    pt = hit_view.from_window(mousepoint)
                    hit_view.mouse_up(e.button, pt)
                down_in_view = None
                event_flag = True
            elif e.type == pygame.MOUSEMOTION:
                if down_in_view and down_in_view.draggable:
                    pt = down_in_view.from_window(mousepoint)
                    down_in_view.mouse_drag(pt, e.rel)
                else:
                    scene.current.mouse_motion(mousepoint)
                event_flag = True
            elif e.type == pygame.KEYDOWN:
                if focus.view:
                    focus.view.key_down(e.key, e.unicode)
                else:
                    scene.current.key_down(e.key, e.unicode)
            elif e.type == pygame.KEYUP:
                if focus.view:
                    focus.view.key_up(e.key)
                else:
                    scene.current.key_up(e.key)
        if event_flag:
            print 'event'
            scene.current.update(dt / 1000.0)
            scene.current.draw()
            window_surface.blit(scene.current.surface, (0, 0))
            pygame.display.flip()
            event_flag = False
        
        if ui_quit:
            pygame.quit()
            import sys
            sys.exit()
