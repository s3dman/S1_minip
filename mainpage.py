import dearpygui.dearpygui as dpg
import config

import loginpage

def mainpage():
    with dpg.window(tag="mainpage",width=config.W, height=config.H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        dpg.add_text("this is the mainpage")
        dpg.add_button(label="go to loginpage",callback=lambda:
                       config.window_handler("mainpage",loginpage.loginpage))
    dpg.set_primary_window('mainpage',True)