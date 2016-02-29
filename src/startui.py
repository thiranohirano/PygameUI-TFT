'''
Created on 2016/02/29

@author: hirano
'''
import pygame
import pygameui as ui
import pygameui.window as window
import VirtualKeyboardPygameUI as vkeyboard
import pygameui_myscene as myscene
import time
import threading
import socket
import sys
from subprocess import PIPE, Popen

LABEL_H = 30
BUTTON_W = 210
BUTTON_H = 60
MARGIN = 20
SMALL_MARGIN = 10

class StartUI(myscene.MyScene):
    def __init__(self, sm):
        myscene.MyScene.__init__(self)
        self.sm = sm
#         self.mainframe = pygameui_mainframe.MainFrame()
#         self.add_child(self.mainframe)
        
        y=MARGIN
        ip_label = ui.Label(ui.Rect(MARGIN, y, window.rect.w - MARGIN * 2, LABEL_H), self.get_ip())
        self.add_child_in_frame(ip_label)
        
        x = MARGIN
        y += LABEL_H + MARGIN;
        self.vkeyboard_button = ui.Button(ui.Rect(MARGIN, y, BUTTON_W, BUTTON_H), 'VKeyboard')
        self.vkeyboard_button.on_clicked.connect(self.gpi_button_click)
        self.add_child_in_frame(self.vkeyboard_button)
        
        x += BUTTON_W + MARGIN
        self.wifi_button = ui.Button(ui.Rect(250, y, BUTTON_W, BUTTON_H), 'Wifi...')
        self.wifi_button.on_clicked.connect(self.wifi_button_click)
        self.add_child_in_frame(self.wifi_button)
 
        x = MARGIN
        y += BUTTON_H + MARGIN
        self.reboot_button = ui.Button(ui.Rect(MARGIN, y, BUTTON_W, BUTTON_H), 'Reboot')
        self.reboot_button.on_clicked.connect(self.reboot_button_click)
        self.add_child_in_frame(self.reboot_button)
 
        x += BUTTON_W + MARGIN
        self.shutdown_button = ui.Button(ui.Rect(250, y, BUTTON_W, BUTTON_H), 'Shutdown')
        self.shutdown_button.on_clicked.connect(self.shutdown_button_click)
        self.add_child_in_frame(self.shutdown_button)
 
    def gpi_button_click(self, btn, mbtn):
        self.vkeyboard=vkeyboard.show_vkeyboard(self.input_vkeyboard, "hoge")
            
    def wifi_button_click(self, btn, mbtn):
        self.sm.use_scene(1)
 
    def input_vkeyboard(self,vkeyboard, text):
        print text
        
    def reboot_button_click(self, btn, mbtn):
#         self.add_fullscreen_label('Rebooting...')
        self.rm_allchildren_in_frame()
        threading.Timer(1, self.restart_proccess).start()
    
    def restart_proccess(self):
        #         self.restart()
        self.dummyrestart()
        pygame.quit()
        sys.exit()
        
    def shutdown_button_click(self, btn, mbtn):
        self.add_fullscreen_label('Shutting Down...')
        threading.Timer(1, self.shutdown_proccess).start()
        
    def shutdown_proccess(self):
#         self.shutdown()
        self.dummyrestart()
        pygame.quit()
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
        ui.Scene.layout(self)