import dearpygui.dearpygui as dpg

W,H = 1280,720

def window_handler(wdt,wcf):
    dpg.delete_item(wdt)
    wcf()

def ui_center(a,*args):
    for item in args:
        print(dpg.get_item_rect_size(item))
    # w = range[1]-range[0]
    # n = len(args)
    # for item in args:
    #     print("pos:",dpg.get_item_pos(item))

