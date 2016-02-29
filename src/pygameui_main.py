#!/usr/bin/env python

import sys
import os


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pygame
import pygameui as ui
import startui
import pifi_pygameui
import pygameuitheme

# os.putenv('SDL_FBDEV', '/dev/fb1')
# os.putenv('SDL_MOUSEDRV', 'TSLIB')
# os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

class SceneManager(object):
    def __init__(self):
        self.scenes = []

    def append_scene(self, scene):
        self.scenes.append(scene)
        
    def use_scene(self, index):
        ui.scene.pop()
        ui.scene.push(self.scenes[index])

if __name__ == '__main__':
    ui.init('pygameui ', (480, 320))
#     pygame.mouse.set_visible(False)
    pygameuitheme.set_theme()
    sm = SceneManager()
    sm.append_scene(startui.StartUI(sm))
    sm.append_scene(pifi_pygameui.Pifi_pygameui(sm))
    sm.use_scene(0)
    ui.run()