'''
Created on 2016/02/29

@author: hirano
'''
import pygameui as ui
import pygameui.window as window

class MainFrame(ui.view.View):
    def __init__(self):
        ui.view.View.__init__(self, ui.Rect(0,0, window.rect.w, window.rect.h))
#         self._enabled = False
        