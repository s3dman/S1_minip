import dearpygui.dearpygui as dpg
import config
import theme
import local_dh

stock = None

def page_handler(wdt,s,hr):
    global stock
    stock = s
    config.window_handler(wdt,stockpage,hr)

def stockpage():

    print(stock)
    db = local_dh.SymbolGet()

    ui = {"g":[], "l":{}, "b":{}, "i":{}}

    with dpg.group(tag='stockpage',parent='main'):
        ui['l']['stockname'] = dpg.add_text(label=db[stock])
    ui['g'] += config.ui_center('stockpage',2)
    dpg.bind_item_font(ui['l']['stockname'],theme.font_registry.JBM[35])
