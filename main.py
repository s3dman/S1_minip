import dearpygui.dearpygui as dpg

import mainpage

dpg.create_context()
import config

dpg.bind_font(f1)
dpg.show_font_manager()
# ====================================================

# calling mainpage
mainpage.mainpage()
# ====================================================
dpg.create_viewport(title='minip', width=config.W, height=config.H)
dpg.setup_dearpygui()

dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
