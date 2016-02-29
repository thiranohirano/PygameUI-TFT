from pygameui import *
from string import maketrans

Uppercase = maketrans("abcdefghijklmnopqrstuvwxyz`1234567890-=[]\;\',./",
  'ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+{}|:"<>?')

class VirtualKeyboardUIView(dialog.DialogView):
    def onekey_clicked(self, btn, mbtn):
        if btn.shiftkey:
            if self.shifted:
                self.shifted = False
                btn.blurred()
                for key in self.keys:
                    if key.special == False:
                        key.text = key.default_caption
            else:
                self.shifted = True
                btn.focused()
                for key in self.keys:
                    if key.special == False:
                        key.text = key.text.translate(Uppercase)
        else:
            if btn.special == False:
                self.input_field.text += btn.text
                self.input_field.focus()
            else:
                if btn.spacekey:
                    self.input_field.text += ' '
                    self.input_field.focus()
                if btn.bskey:
                    self.input_field.text = self.input_field.text[:-1]
                    self.input_field.focus()
                if btn.enter:
                    self.return_text = self.input_field.text
                    self.on_inputed(self, self.return_text)
                    self.dismiss_gc()
                if btn.escape:
                    self.return_text = ''
                    self.dismiss_gc()
                    
    def dismiss_gc(self):
        self.dismiss()
        import gc
        del self
        gc.collect()
    
    def __init__(self, text = ''):
        self.shifted = False
        self.return_text = text
        self.startup = 0
        
        dialog.DialogView.__init__(self, pygame.Rect(0, 0, 1, 1))
        self.on_inputed = callback.Signal()
        
        self.input_field = textfield.TextField(pygame.Rect(0,0,window.rect.w - 30,theme.current.label_height), "", "")
        self.input_field.valign = label.TOP
        self.input_field.text = text
        self.add_child(self.input_field)
        
        self.keys = []
        margin_x = 2
        margin_y = 2
        
        self.keyW = int(window.rect.w / 12) - 2
        self.keyH = int(window.rect.h / 8 + 0.5)
        
        x = 0
        y = theme.current.label_height + margin_y
        row = ['1','2','3','4','5','6','7','8','9','0','-','=']
        for item in row:
            onekey = VKey(pygame.Rect(x,y,self.keyW,self.keyH) ,item)
            onekey.on_clicked.connect(self.onekey_clicked)
            self.keys.append(onekey)
            self.add_child(onekey)
            x += self.keyW + margin_x
            
        x=0
        y += self.keyH + margin_y
        row = ['q','w','e','r','t','y','u','i','o','p','[',']']
        for item in row:
            onekey = VKey(pygame.Rect(x,y,self.keyW,self.keyH) ,item)
            onekey.on_clicked.connect(self.onekey_clicked)
            self.keys.append(onekey)
            self.add_child(onekey)
            x += self.keyW + margin_x
            
        x=0
        y += self.keyH + margin_y
        row = ['a','s','d','f','g','h','j','k','l',';','\'','`']
        for item in row:
            onekey = VKey(pygame.Rect(x,y,self.keyW,self.keyH) ,item)
            onekey.on_clicked.connect(self.onekey_clicked)
            self.keys.append(onekey)
            self.add_child(onekey)
            x += self.keyW + margin_x
            
        x=self.keyW/2 
        y+= self.keyH + margin_y
        row = ['z','x','c','v','b','n','m',',','.','/','\\']
        
        for item in row:
            onekey = VKey(pygame.Rect(x,y,self.keyW,self.keyH) ,item)
            onekey.on_clicked.connect(self.onekey_clicked)
            self.keys.append(onekey)
            self.add_child(onekey)
            x += self.keyW + margin_x
            
        x=0
        y+= self.keyH + margin_y
        onekey = VKey(pygame.Rect(x,y,self.keyW * 2.5,self.keyH), 'Shift')
        onekey.special = True
        onekey.shiftkey = True
        onekey.on_clicked.connect(self.onekey_clicked)
        self.keys.append(onekey)
        self.add_child(onekey)
        
        x+= onekey.frame.w + self.keyW/6
        onekey = VKey(pygame.Rect(x,y,self.keyW * 5,self.keyH), 'Space')
        onekey.special = True
        onekey.spacekey = True
        onekey.on_clicked.connect(self.onekey_clicked)
        self.keys.append(onekey)
        self.add_child(onekey)
        
        x+=onekey.frame.w + self.keyW/6
        onekey = VKey(pygame.Rect(x,y,self.keyW * 2.5,self.keyH), 'Enter')
        onekey.special = True
        onekey.enter = True
        onekey.on_clicked.connect(self.onekey_clicked)
        self.keys.append(onekey)
        self.add_child(onekey)
        
        x+=onekey.frame.w + self.keyW/3
        onekey = VKey(pygame.Rect(x,y,self.keyW * 1.2,self.keyH), '<-')
        onekey.special = True
        onekey.bskey = True
        onekey.on_clicked.connect(self.onekey_clicked)
        self.keys.append(onekey)
        self.add_child(onekey)
            
        onekey = VKey(pygame.Rect(window.rect.w - 30, 0, 30 - 2, theme.current.label_height - 1), 'X')
        onekey.special = True
        onekey.escape = True
        onekey.on_clicked.connect(self.onekey_clicked)
        self.keys.append(onekey)
        self.add_child(onekey)

    def update(self,dt):
        self.startup += dt
        if self.startup < 0.5:
            self.input_field.text = self.return_text
            
        self.input_field.label.font = pygame.font.SysFont('Courier New', 16)
        self.input_field.layout()
        for key in self.keys:
            key.font = pygame.font.SysFont('Courier New', 20, bold= True)
            key.layout()

    def layout(self):
        self.frame.w = max(100, window.rect.w)
        self.frame.h = max(100, window.rect.h)

        dialog.DialogView.layout(self)

    def _dismiss(self, btn, mbtn):
        self.dismiss()

    def key_down(self, key, code):
        dialog.DialogView.key_down(self, key, code)
        if key == pygame.K_RETURN:  # ~ ok
            self.dismiss()

class VKey(button.Button):
    def __init__(self, frame, caption):
        button.Button.__init__(self, frame, caption)
        self.default_caption = caption
        self.special = False
        self.enter = False
        self.bskey = False
        self.fskey = False
        self.spacekey = False
        self.escape = False
        self.shiftkey = False

def show_vkeyboard(slot, text = ''):
    vkeyboard_view = VirtualKeyboardUIView(text)
    scene.current.add_child(vkeyboard_view)
    vkeyboard_view.on_inputed.connect(slot)
    vkeyboard_view.focus()
    vkeyboard_view.center()
    return vkeyboard_view

