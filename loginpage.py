import dearpygui.dearpygui as dpg
import config

import mainpage

def loginpage():
    with dpg.window(tag="loginpage",width=config.W, height=config.H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        dpg.add_text("this is the loginpage")
        dpg.add_button(label="go to mainpage",callback=lambda:
                       config.window_handler("loginpage",mainpage.mainpage))
    dpg.set_primary_window('loginpage',True)
