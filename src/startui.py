'''
Created on 2016/02/29

@author: hirano
'''
import sys
import pygameui as ui
from pygameui import *
import VirtualKeyboardPygameUI
import mycolors
from pygameui.colors import black_color
from subprocess import *
import time
import threading
import socket

LABEL_H = 30
BUTTON_W = 210
BUTTON_H = 60
MARGIN = 20
SMALL_MARGIN = 10

class StartUI(ui.Scene):
    def __init__(self, sm):
        ui.Scene.__init__(self)
        self.sm = sm
        self.mainlabel = ui.Label(ui.Rect(0, 0, window.rect.w , window.rect.h), "")
        self.add_child(self.mainlabel)
        
        y=MARGIN
        ip_label = ui.Label(ui.Rect(MARGIN, y, window.rect.w - MARGIN * 2, LABEL_H), self.get_ip())
        self.add_child(ip_label)
        
        x = MARGIN
        y += LABEL_H + MARGIN;
        self.on17_button = ui.Button(ui.Rect(MARGIN, y, BUTTON_W, BUTTON_H), 'VKeyboard')
        self.on17_button.on_clicked.connect(self.gpi_button_click)
        self.add_child(self.on17_button)
        
        x += BUTTON_W + MARGIN
        self.wifi_button = ui.Button(ui.Rect(250, y, BUTTON_W, BUTTON_H), 'Wifi...')
        self.wifi_button.on_clicked.connect(self.wifi_button_click)
        self.add_child(self.wifi_button)
 
        x = MARGIN
        y += BUTTON_H + MARGIN
        self.reboot_button = ui.Button(ui.Rect(MARGIN, y, BUTTON_W, BUTTON_H), 'Reboot')
        self.reboot_button.on_clicked.connect(self.reboot_button_click)
        self.add_child(self.reboot_button)
 
        x += BUTTON_W + MARGIN
        self.shutdown_button = ui.Button(ui.Rect(250, y, BUTTON_W, BUTTON_H), 'Shutdown')
        self.shutdown_button.on_clicked.connect(self.shutdown_button_click)
        self.add_child(self.shutdown_button)
 
    def gpi_button_click(self, btn, mbtn):
        self.vkeyboard=VirtualKeyboardPygameUI.show_vkeyboard(self.input_vkeyboard, "hoge")
            
    def wifi_button_click(self, btn, mbtn):
        self.sm.use_scene(1)
 
    def input_vkeyboard(self,vkeyboard, text):
        print text
        
    def reboot_button_click(self, btn, mbtn):
        label = ui.Label(ui.Rect(0,0, window.rect.w, window.rect.h), 'Rebooting...')
        self.add_child(label)
        threading.Timer(1, self.restart_proccess).start()
    
    def restart_proccess(self):
        pygame.quit()
        #         self.restart()
        self.dummyrestart()
        sys.exit()
        
    def shutdown_button_click(self, btn, mbtn):
        label = ui.Label(ui.Rect(0,0, window.rect.w, window.rect.h), 'Shutting Down...')
        self.add_child(label)
        threading.Timer(1, self.shutdown_proccess).start()
        
    def shutdown_proccess(self):
        pygame.quit()
#         self.shutdown()
        self.dummyrestart()
        sys.exit()
        
    # Get Your External IP Address
    def get_ip(self):
        ip_msg = "Not connected"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            s.connect(('<broadcast>', 0))
            ip_msg="IP:" + s.getsockname()[0]
        except Exception:
            pass
        return ip_msg

    # Restart Raspberry Pi
    def restart(self):
        command = "/usr/bin/sudo /sbin/shutdown -r now"
        process = Popen(command.split(), stdout=PIPE)
        output = process.communicate()[0]
        return output
    
    def dummyrestart(self):
        time.sleep(1)

# Shutdown Raspberry Pi
    def shutdown(self):
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        process = Popen(command.split(), stdout=PIPE)
        output = process.communicate()[0]
        return output

 
    def update(self, dt):
        ui.Scene.update(self, dt)
        
    def layout(self):
        self.mainlabel.background_color = black_color
        self.mainlabel.border_color = mycolors.belize_hole
        self.mainlabel.border_widths = 8
        ui.Scene.layout(self)