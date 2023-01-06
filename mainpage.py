import dearpygui.dearpygui as dpg
import config
import theme

import loginpage

def mainpage():
    ui = { "l":{}, "b":{} }

    with dpg.window(tag="mainpage",width=config.W, height=config.H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        ui['b']['loginpage'] = dpg.add_button(label="go to loginpage",callback=lambda:
                       config.window_handler("mainpage",loginpage.loginpage))
        with dpg.group(horizontal=True) as x:
            ui['l']['a'] = dpg.add_text("this is text1")
            ui['l']['b'] = dpg.add_text("this may be text2")
            ui['l']['c'] = dpg.add_text("text3")
        dpg.bind_item_font(ui['b']['loginpage'],theme.font_registry.JBM[25])
        config.ui_center(None,x)
    dpg.set_primary_window('mainpage',True)