import dearpygui.dearpygui as dpg
import config
import theme

import mainpage

def loginpage():
    ui = {"h":[], "l":{}, "b":{}, "i":{}}

    with dpg.group(tag='loginpage',parent='main'):

        with dpg.group(tag='bruh'):
            ui["l"]["informer"] = dpg.add_text("LOGIN")
            ui["b"]["mainpage"] = dpg.add_button(label="go to mainpage",width=200,height=100,
                callback=lambda: config.window_handler("loginpage",mainpage.mainpage,ui['h']))

        ui['h'] += config.ui_center('bruh',2)
        dpg.bind_item_font(ui["b"]["mainpage"],theme.font_registry.JBM[25])
