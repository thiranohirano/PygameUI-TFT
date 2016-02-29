'''
Created on 2016/02/26

@author: hirano
'''
from pygameui_main import *
import pygameui as ui
from pygameui.colors import *
import threading
import time
import mycolors
from VirtualKeyboardPygameUI import *

LIST_WIDTH = 380
MARGIN = 20
    
class Pifi_pygameui(ui.Scene):
    '''
    classdocs
    '''
    def __init__(self, sm):
        ui.Scene.__init__(self)
        self.sm = sm
        self.startsearch = True
        self.searched = False
        self.aps = []
        self.mainlabel = ui.Label(ui.Rect(0, 0, window.rect.w , window.rect.h), "")
        
        self.add_child(self.mainlabel)
        
        self.label1 = ui.Label(ui.Rect(MARGIN , MARGIN, window.rect.w - MARGIN * 2, theme.current.label_height), "APs Searching...")
        self.add_child(self.label1)
        
        self.back_button = ui.Button(ui.Rect(window.rect.w - 100, window.rect.h - MARGIN - theme.current.label_height, 80, theme.current.label_height), 'Back')
        self.back_button.on_clicked.connect(self.back_button_click)
        self.add_child(self.back_button)
        
        self.spinner = ui.SpinnerView(ui.Rect(
            (window.rect.w - ui.SpinnerView.size) / 2,
            (window.rect.h - ui.SpinnerView.size) / 2,
            0, 0))
        self.add_child(self.spinner)
        self.scroll_list = None
        
    def back_button_click(self, btn, mbtn):
        self.sm.use_scene(0)    
    
    def item_selected(self, list_view, item, index):
        print str(index)
        show_vkeyboard(self.input_promptpassword)
        
    def input_promptpassword(self, vkeyboard, text):
        print text
        
    def search_proccess(self):
        count = 0
        for _ in range(10):
            time.sleep(0.5)
            count += 1
            print 'count: %d' % (count )
            self.aps.append('count: %d' % (count ))
        self.spinner.rm()
#         self.pifi_ui.sm.use_scene(0)
        self.searched = True
        
    def update(self, dt):
        ui.Scene.update(self, dt)
        if self.startsearch:
            self.rm_child(self.scroll_list)
            self.add_child(self.spinner)
            search_proc = threading.Thread(target=self.search_proccess)
            search_proc.setDaemon(True)
            search_proc.start()
            self.startsearch = False
            
        if self.searched:
            labels = [ui.Label(ui.Rect(
            0, 0, LIST_WIDTH, theme.current.label_height), item, halign=ui.LEFT)
            for item in self.aps]
            list_view = ui.ListView(ui.Rect(0, 0, LIST_WIDTH, 400), labels)
            list_view.on_selected.connect(self.item_selected)
            self.scroll_list = ui.ScrollView(ui.Rect(
                50,  MARGIN * 2 + theme.current.label_height,
                LIST_WIDTH, 180), list_view)
            self.add_child(self.scroll_list)
            self.searched = False
        
    def layout(self):
        self.mainlabel.background_color = black_color
        self.mainlabel.border_color = mycolors.belize_hole
        self.mainlabel.border_widths = 8
        
        ui.Scene.layout(self)