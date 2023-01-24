import dearpygui.dearpygui as dpg
import config
import theme
import loginpage
import mainpage
import settingspage
import authentication
import local_dh

pW,pH = 500,200
stocklist = local_dh.SymbolGet()
def add_investment():
    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    def stockcheck():
        if dpg.get_value(ui['i']['stockname']) in stocklist:
            print("yes")
        else:
            print("No")

    with dpg.window(tag='popup',width=pW,height=pH,pos=(int(config.W/2-pW/2),int(config.H/2-pH/2)),no_collapse=True,no_move=True,no_title_bar=True,modal=True):
        dpg.add_spacer(height=7)
        with dpg.group(tag='titlegroup'):
            ui['l']['investment_title'] = dpg.add_text("Add investment")
        dpg.add_spacer(height=7)
        with dpg.group(tag='popupgroup'):
            with dpg.group(tag='stock',horizontal=True):
                ui['i']['stockname'] = dpg.add_input_text(hint="Stock",width=200)
                ui['b']['stockcheck'] = dpg.add_button(label="Fetch",width=200,callback=stockcheck)
            with dpg.group(tag='qty',horizontal=True):
                ui['i']['qty'] = dpg.add_input_text(hint="Quantity",width=200)
                ui['b']['qtyp'] = dpg.add_button(label="+")
                ui['b']['qtym'] = dpg.add_button(label="-")
            with dpg.group(tag='price',horizontal=True):
                ui['i']['price'] = dpg.add_input_text(hint='Buy Price',width=200)
                ui['b']['pricecheck'] = dpg.add_button(label="Get Current Price",width=200)
            with dpg.group(tag='buttons',horizontal=True):
                ui['b']['cancel'] = dpg.add_button(label="Cancel",width=100,callback=lambda:config.window_handler("popup",None,ui['g'],popup=True))
                ui['l']['status_info'] = dpg.add_text(show=False)
                # dpg.add_spacer(width=190)
                ui['b']['add'] = dpg.add_button(label="Add",width=100,callback=lambda:config.window_handler("popup",None,ui['g'],popup=True))
    ui['g'] += config.ui_center('titlegroup',0,W=500,H=250)
    ui['g'] += config.ui_center('popupgroup',0,W=500,H=250)

def portfoliopage():

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='portfoliopage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("portfoliopage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=410,callback=lambda: config.window_handler("portfoliopage",mainpage.mainpage,ui['g']))
            ui['b']['settings'] = dpg.add_button(label="Settings",width=410,callback=lambda: config.window_handler("portfoliopage",settingspage.settingspage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['portfolio'] = dpg.add_text(f"{authentication.curr_username}'s Portfolio")
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
    dpg.bind_item_font(ui['l']['portfolio'],theme.font_registry.JBM[30])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
    dpg.bind_item_font(ui['b']['add_button'],theme.font_registry.JBM[30])
