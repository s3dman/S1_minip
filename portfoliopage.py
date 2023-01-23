import dearpygui.dearpygui as dpg
import config
import theme
import loginpage
import mainpage
import settingspage

def add_investment():
    with dpg.window(tag='popup',width=500,height=500,pos=(390,110),no_collapse=True,no_move=True,no_title_bar=True,modal=True):
        dpg.add_button(label="cancel",callback=lambda:dpg.delete_item("popup"))

def portfoliopage():

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='portfoliopage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("portfoliopage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=410,callback=lambda: config.window_handler("portfoliopage",mainpage.mainpage,ui['g']))
            ui['b']['settings'] = dpg.add_button(label="Settings",width=410,callback=lambda: config.window_handler("portfoliopage",settingspage.settingspage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['portfolio'] = dpg.add_text("users Portfolio")
        with dpg.group(tag='graph'):
            with dpg.plot(width=1250,height=400,anti_aliased=True):
                dpg.add_plot_axis(dpg.mvXAxis,tag='xaxis',time=True)
                dpg.add_plot_axis(dpg.mvYAxis,label="USD",tag='yaxis')
        with dpg.group(tag='investment'):
            ui['b']['add_button'] = dpg.add_button(label="add",callback=add_investment)

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    ui['g'] += config.ui_center('graph',0)
    ui['g'] += config.ui_center('investment',0)
    dpg.bind_item_font(ui['l']['portfolio'],theme.font_registry.JBM[35])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
    dpg.bind_item_font(ui['b']['add_button'],theme.font_registry.JBM[30])
