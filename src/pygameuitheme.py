from pygameui import *
from pygameui.colors import *
import mycolors

def set_theme():
    
    theme.current.set(class_name='Scene',
                    state='normal',
                    key='background_color',
                    value=black_color)
    
    theme.current.set(class_name='DialogView',
                    state='normal',
                    key='background_color',
                    value=(black_color, black_color))
    
    theme.current.set(class_name='Label',
                state='normal',
                key='text_shadow_color',
                value=None)
    theme.current.set(class_name='Label',
                state='normal',
                key='font',
                value=pygame.font.SysFont('Courier New', 28))
    theme.current.set(class_name='Label',
                state='normal',
                key='background_color',
                value=black_color)
    theme.current.set(class_name='Label',
                state='selected',
                key='background_color',
                value=mycolors.peter_river)
    theme.current.set(class_name='Label',
                state='normal',
                key='text_color',
                value=mycolors.clouds)
    theme.current.set(class_name='Label',
                state='selected',
                key='text_color',
                value=mycolors.wet_asphalt)
    
    theme.current.set(class_name='Button',
                state='normal',
                key='text_color',
                value=mycolors.clouds)
    theme.current.set(class_name='Button',
                state='focused',
                key='text_color',
                value=mycolors.wet_asphalt)
    theme.current.set(class_name='Button',
                state='normal',
                key='font',
                value=pygame.font.SysFont('Courier New', 24, bold= True))
    theme.current.set(class_name='Button',
                state='normal',
                key='background_color',
                value=(black_color, black_color))
    theme.current.set(class_name='Button',
                    state='focused',
                    key='background_color',
                    value=mycolors.peter_river)
    theme.current.set(class_name='Button',
                state='normal',
                key='border_widths',
                value=2)
    theme.current.set(class_name='Button',
                state='normal',
                key='border_color',
                value=mycolors.belize_hole)
    
    theme.current.set(class_name='TextField',
                state='normal',
                key='label.background_color',
                value=(white_color,near_white_color))
    theme.current.set(class_name='TextField',
                state='focused',
                key='label.background_color',
                value=(white_color,near_white_color))
    theme.current.set(class_name='TextField',
                state='focused',
                key='label.text_color',
                value=mycolors.midnight_blue)
    theme.current.set(class_name='TextField',
                state='normal',
                key='label.text_color',
                value=mycolors.midnight_blue)
    
    theme.current.set(class_name='ScrollbarThumbView',
                    state='focused',
                    key='background_color',
                    value=mycolors.peter_river)
    theme.current.set(class_name='ScrollbarView',
                    state='normal',
                    key='border_color',
                    value=mycolors.belize_hole)
    theme.current.set(class_name='ScrollView',
                    state='normal',
                    key='background_color',
                    value=mycolors.asbestos)
    theme.current.set(class_name='ScrollView',
                    state='normal',
                    key='border_color',
                    value=mycolors.belize_hole)
    theme.current.set(class_name='ScrollView',
                    state='normal',
                    key='border_widths',
                    value=3)
    
    theme.current.set(class_name='MainFrame',
                    state='normal',
                    key='background_color',
                    value=black_color)
    theme.current.set(class_name='MainFrame',
                    state='normal',
                    key='border_color',
                    value=mycolors.belize_hole)
    theme.current.set(class_name='MainFrame',
                    state='normal',
                    key='border_widths',
                    value=8)
