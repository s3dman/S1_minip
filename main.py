import dearpygui.dearpygui as dpg
import config

import mainpage

dpg.create_context()
# ====================================================

# calling mainpage
mainpage.mainpage()

# ====================================================
dpg.create_viewport(title='minip', width=config.W, height=config.H)
dpg.setup_dearpygui()

dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
