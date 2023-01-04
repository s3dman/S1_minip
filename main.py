import dearpygui.dearpygui as dpg

import mainpage
import container_test

dpg.create_context()

W,H = 1280,720

def window1():
    with dpg.window(tag="window1",width=W, height=H, no_resize=True , no_move=False, no_close=True, no_collapse=True):
        dpg.add_button(label="bruh",width=100,height=100,callback=handler1,pos=[100,100])
    dpg.set_primary_window('window1',True)


def handler1():
    pass
    # dpg.delete_item('window1')
    # mainpage.mainpage()


window1()

dpg.create_viewport(title='minip', width=W, height=H)
dpg.setup_dearpygui()

dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
