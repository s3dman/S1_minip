import dearpygui.dearpygui as dpg

W,H = 1280,720

def window_handler(wdt,wcf):
    dpg.delete_item(wdt)
    wcf()
