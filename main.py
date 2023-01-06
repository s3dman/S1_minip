import dearpygui.dearpygui as dpg
import config


dpg.create_context()
dpg.create_viewport(title='minip', width=config.W, height=config.H)
dpg.set_viewport_max_height(720)
dpg.set_viewport_max_width(1280)
dpg.set_viewport_min_height(720)
dpg.set_viewport_min_width(1280)

# create viewport then import registries
import theme
theme.font_registry.font_init()
dpg.bind_font(theme.font_registry.JBM[20])

# ====================================================

import loginpage
loginpage.loginpage()

# ====================================================

dpg.setup_dearpygui()

dpg.show_viewport()
dpg.start_dearpygui()

dpg.destroy_context()
