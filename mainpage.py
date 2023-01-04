import dearpygui.dearpygui as dpg

W,H = 1280,720

def mainpage():
    with dpg.window(tag="window2",width=W, height=H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        pass
        # dpg.add_date_picker()
    dpg.set_primary_window('window2',True)