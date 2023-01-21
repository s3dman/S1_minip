import dearpygui.dearpygui as dpg
import config
import theme
import local_dh

# stock 
# def page_handler(sender):
#     global stock
#     stock = str(dpg.get_item_label(sender)).split()[0]
#     config.window_handler("mainpage",stockpage,)

def stockpage():

    db = local_dh.SymbolGet()

    ui = {"g":[], "l":{}, "b":{}, "i":{}}

    with dpg.group(tag='stockpage',parent='main'):
        ui['l']['stockname'] = dpg.add_text(label=db[stock])
    ui['g'] += config.ui_center('stockpage',2)
    dpg.bind_item_font(ui['l']['stockname'],theme.font_registry.JBM[35])
