import dearpygui.dearpygui as dpg
import config
import theme
import loginpage
import mainpage
import settingspage

def portfoliopage():

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='portfoliopage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("portfoliopage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=410,callback=lambda: config.window_handler("portfoliopage",mainpage.mainpage,ui['g']))
            ui['b']['settings'] = dpg.add_button(label="Settings",width=410,callback=lambda: config.window_handler("portfoliopage",settingspage.settingspage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['portfolio'] = dpg.add_text("portfolio")

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    dpg.bind_item_font(ui['l']['portfolio'],theme.font_registry.JBM[35])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
