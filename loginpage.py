import dearpygui.dearpygui as dpg
import config
import theme

import mainpage

def loginpage():
    ui = { "l":{}, "b":{} }

    with dpg.window(tag="loginpage",width=config.W, height=config.H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        ui["l"]["informer"] = dpg.add_text("LOGIN")
        ui["b"]["mainpage"] = dpg.add_button(label="go to mainpage",width=200,height=100,
            callback=lambda: config.window_handler("loginpage",mainpage.mainpage))
        dpg.bind_item_font(ui["b"]["mainpage"],theme.font_registry.JBM[25])
    dpg.set_primary_window('loginpage',True)
