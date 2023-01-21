import dearpygui.dearpygui as dpg
import config
import theme
import loginpage
import mainpage
import portfoliopage

def settingspage():

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='settingspage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("settingspage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=410,callback=lambda: config.window_handler("settingspage",mainpage.mainpage,ui['g']))
            ui['b']['portfolio'] = dpg.add_button(label="Portfolio",width=410,callback=lambda: config.window_handler("settingspage",portfoliopage.portfoliopage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['settings'] = dpg.add_text("settings")

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    dpg.bind_item_font(ui['l']['settings'],theme.font_registry.JBM[35])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
