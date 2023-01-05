import dearpygui.dearpygui as dpg

JBM = {}

def font_init():
    global JBM
    with dpg.font_registry():
        for i in range(10,26,5):
            JBM[i] = dpg.add_font("./assets/JetBrainsMono/JetBrainsMono-Bold.ttf", i)
