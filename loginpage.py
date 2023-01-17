import dearpygui.dearpygui as dpg
import config
import theme

import mainpage

def loginpage():
    ui = { "l":{}, "b":{} }

    with dpg.group(tag='loginpage',parent='main'):

        ui["l"]["informer"] = dpg.add_text("LOGIN")
        ui["b"]["mainpage"] = dpg.add_button(label="go to mainpage",width=200,height=100,
            callback=lambda: config.window_handler("loginpage",mainpage.mainpage))
        dpg.bind_item_font(ui["b"]["mainpage"],theme.font_registry.JBM[25])
