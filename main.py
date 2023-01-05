import dearpygui.dearpygui as dpg
import config


dpg.create_context()
dpg.create_viewport(title='minip', width=config.W, height=config.H)

# create viewport then import registries
import theme
theme.font_registry.font_init()

# ====================================================

import loginpage
loginpage.loginpage()

# ====================================================

dpg.setup_dearpygui()

dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
