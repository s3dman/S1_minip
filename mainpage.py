import dearpygui.dearpygui as dpg
import config
import theme

import loginpage

def mainpage():
    ui = { "l":{}, "b":{} }

    with dpg.window(tag="mainpage",width=config.W, height=config.H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        ui['l']['informer'] = dpg.add_text("this is the mainpage")
        ui['b']['loginpage'] = dpg.add_button(label="go to loginpage",callback=lambda:
                       config.window_handler("mainpage",loginpage.loginpage))
        dpg.bind_item_font(ui['b']['loginpage'],theme.font_registry.JBM[25])
    dpg.set_primary_window('mainpage',True)