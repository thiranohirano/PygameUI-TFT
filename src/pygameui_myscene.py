'''
Created on 2016/02/29

@author: hirano
'''
import pygameui as ui
import pygameui.window as window
import pygameui_mainframe as mainframe
import copy

class MyScene(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)
        self.mainframe = mainframe.MainFrame()
        self.add_child(self.mainframe)
        
    def add_child_in_frame(self, child):
        self.mainframe.add_child(child)
        
    def rm_child_in_frame(self, child):
        self.mainframe.rm_child(child)
        
    def add_fullscreen_label(self, text):
        label = ui.Label(ui.Rect(0,0, window.rect.w, window.rect.h), text)
        self.add_child(label)
        return label
    
    def rm_allchildren_in_frame(self):
        mychildren = copy.copy(self.mainframe.children)
        for child in mychildren:
            self.rm_child_in_frame(child)