import dearpygui.dearpygui as dpg
import config
import theme

import loginpage


def mainpage():
    ui = {"g":[], "l":{}, "b":{}, "i":{}}

    with dpg.group(tag='mainpage',parent='main'):
        ui['b']['loginpage'] = dpg.add_button(label="go to loginpage",callback=lambda:
                       config.window_handler("mainpage",loginpage.loginpage,ui['g']))
        with dpg.group(tag='temp1'):
            with dpg.table(borders_outerH=True,borders_outerV=True,width=1000,height=600,header_row=False,scrollY=True):
                dpg.add_table_column()
                for i in range(150):
                    with dpg.table_row():
                        dpg.add_button(label=f"Buttom: {i}",width=1000)
        ui['g'] += config.ui_center('temp1',2)
        dpg.bind_item_font(ui['b']['loginpage'],theme.font_registry.JBM[25])