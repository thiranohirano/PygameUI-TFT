'''
Created on 2016/02/26

@author: hirano
'''
import myui as ui
import pygameui.window as window
import pygameui.theme as theme
import VirtualKeyboardPygameUI as vkeyboard
from virtualKeyboard import VirtualKeyboard
import pygameui_myscene as myscene
import pygameui_myspinner as myspinner
import threading
import time
import proccess_spinner

LIST_WIDTH = 380
BUTTON_WIDTH = 80
MARGIN = 20
    
class Pifi_pygameui(myscene.MyScene):
    '''
    classdocs
    '''
    def __init__(self, sm):
        myscene.MyScene.__init__(self)
        self.sm = sm
        self.startsearch = True
        self.searched = False
        self.searching = False
        self.aps = []
        
        self.label1 = ui.Label(ui.Rect(MARGIN , MARGIN, window.rect.w - MARGIN * 2, theme.current.label_height), "Select WiFi network...")
#         self.add_child_in_frame(self.label1)
        
        self.search_button = ui.Button(ui.Rect( MARGIN, window.rect.h - MARGIN - theme.current.label_height, BUTTON_WIDTH + 20, theme.current.label_height), 'Search')
        self.search_button.on_clicked.connect(self.search_button_click)
#         self.add_child_in_frame(self.search_button)
        
        self.back_button = ui.Button(ui.Rect(window.rect.w - BUTTON_WIDTH - MARGIN, window.rect.h - MARGIN - theme.current.label_height, BUTTON_WIDTH, theme.current.label_height), 'Back')
        self.back_button.on_clicked.connect(self.back_button_click)
#         self.add_child_in_frame(self.back_button)
        
#         self.spinner = ui.SpinnerView(ui.Rect(
#             (window.rect.w - ui.SpinnerView.size) / 2,
#             (window.rect.h - ui.SpinnerView.size) / 2,
#             0, 0))
#         self.spinner = myspinner.MySpinner(ui.Rect((window.rect.w - myspinner.MySpinner.size) /2, (window.rect.h - myspinner.MySpinner.size) /2, 0, 0))
#         self.add_child_in_frame(self.spinner)
        self.scroll_list = None
        
        self.init_scene()
        
    def init_scene(self):
        self.add_child_in_frame(self.label1)
        self.add_child_in_frame(self.search_button)
        self.add_child_in_frame(self.back_button)
        if self.scroll_list <> None:
            self.add_child_in_frame(self.scroll_list)
            
    def search_button_click(self, btn, mbtn):
        ps = proccess_spinner.ProccessSpinner(ui.window_surface, 'Scanning for WiFi networks...')
        ps.run(self.search_proccess)
        
    def back_button_click(self, btn, mbtn):
        self.sm.use_scene(0)    
    
    def item_selected(self, list_view, item, index):
        print str(index)
#         vkeyboard.show_vkeyboard(self.input_promptpassword)
        vkey = VirtualKeyboard(ui.window_surface)
        input_key = vkey.run("")
        print input_key
        
#     def input_promptpassword(self, vkeyboard, text):
#         print text
        
    def search_proccess(self):
        self.aps = []
        count = 0
        for _ in range(10):
            time.sleep(0.5)
            count += 1
            print 'count: %d' % (count )
            self.aps.append('count: %d' % (count ))
#         self.spinner.rm()
#         self.pifi_ui.sm.use_scene(0)
        self.searched = True
        
    def update(self, dt):
        ui.Scene.update(self, dt)
        if self.startsearch:
            self.rm_child_in_frame(self.scroll_list)
#             self.add_child_in_frame(self.spinner)
#             self.aps = []
#             search_proc = threading.Thread(target=self.search_proccess)
#             search_proc.setDaemon(True)
#             search_proc.start()
            
            self.startsearch = False
            
        if self.searched:
            labels = [ui.Label(ui.Rect(
            0, 0, LIST_WIDTH, theme.current.label_height), item, halign=ui.LEFT)
            for item in self.aps]
            list_view = ui.ListView(ui.Rect(0, 0, LIST_WIDTH, 400), labels)
            list_view.on_selected.connect(self.item_selected)
            self.scroll_list = ui.ScrollView(ui.Rect(
                50,  MARGIN * 2 + theme.current.label_height,
                LIST_WIDTH, theme.current.label_height * 6), list_view)
            self.add_child_in_frame(self.scroll_list)
            self.searched = False
            
#         if self.searching:
#             ps = proccess_spinner.ProccessSpinner(ui.window_surface)
#             ps.run(self.search_proccess)
#             self.searching = False;
            
#     def proccess(self):
#         self.searching = True
        
    def layout(self):
        self.startsearch = True
        ui.Scene.layout(self)
#         threading.Timer(0.1, self.proccess).start()