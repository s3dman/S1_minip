import dearpygui.dearpygui as dpg
import config
import theme
import local_dh
import mainpage
import loginpage

stock = None
def page_handler(sender):
    global stock
    stock = str(dpg.get_item_label(sender)).split()[0]
    config.window_handler("mainpage",stockpage,mainpage.ui['g'])

def stockpage():
    db = local_dh.SymbolGet()

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='stockpage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=420,callback=lambda: config.window_handler("stockpage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=420,callback=lambda: config.window_handler("stockpage",mainpage.mainpage,ui['g']))
            ui['b']['settings'] = dpg.add_button(label="Settings",width=420,callback=lambda: config.window_handler("stockpage",loginpage.loginpage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['stockname'] = dpg.add_text(db[stock])
        with dpg.group(tag='graph'):
            pass

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    dpg.bind_item_font(ui['l']['stockname'],theme.font_registry.JBM[35])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
