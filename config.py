import dearpygui.dearpygui as dpg
# from main import font_registry


W,H = 1280,720

def window_handler(wdt,wcf):
    dpg.delete_item(wdt)
    wcf()
