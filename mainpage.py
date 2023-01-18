import dearpygui.dearpygui as dpg
import config
import theme

import loginpage


def mainpage():
    ui = {"g":{}, "l":{}, "b":{}, "i":{}}

    with dpg.group(tag='mainpage',parent='main'):

        with dpg.group() as ui['g']['temp1']:
            ui['l']['a'] = dpg.add_text("this is text1")
            ui['b']['loginpage'] = dpg.add_button(label="go to loginpage",callback=lambda:
                           config.window_handler("mainpage",loginpage.loginpage,ui))

        with dpg.group() as ui['g']['temp2']:
            ui['i']['input'] = dpg.add_input_text(width=200)

        config.ui_center(ui['g']['temp1'],2,0.5,0.5)
        config.ui_center(ui['g']['temp2'],2,0.5,0.6)
        dpg.bind_item_font(ui['b']['loginpage'],theme.font_registry.JBM[25])