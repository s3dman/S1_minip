import dearpygui.dearpygui as dpg
import config
import theme
import local_dh
import mainpage
import loginpage
import data_fetch
import settingspage
import multithread

stock = None
def page_handler(sender):
    global stock
    stock = str(dpg.get_item_label(sender)).split()[0]
    config.window_handler("mainpage",stockpage,mainpage.ui['g'])

def graph_update(stock,period,interval):
    date,open,high,low,close = data_fetch.stock_history_period(stock,period,interval)
    dpg.set_value('series',value = (date,open,close,low,high))
    dpg.set_axis_limits_auto('xaxis')
    dpg.set_axis_limits('xaxis',ymax=date[-1],ymin=date[0])
    dpg.fit_axis_data('yaxis')

def graph_print():
    date,open,high,low,close = data_fetch.stock_history_period(stock,"6mo","1d")
    dpg.add_candle_series(dates=date,opens=open,highs=high,closes=close,lows=low,parent='yaxis',time_unit=dpg.mvTimeUnit_Hr,tag='series')
    dpg.set_axis_limits('xaxis',ymax=date[-1],ymin=date[0])
    dpg.fit_axis_data('yaxis')


def info_print():
    temp = data_fetch.stock_info(stock)
    with dpg.group(parent="infotablegroup"):
        dpg.add_spacer(height=10)
        for i in temp:
            if i == 'Summary':
                continue
            dpg.add_text(f"{i} : {temp[i]}")
    dpg.add_spacer(parent='infotablegroup',width=50)
    with dpg.group(parent='infotablegroup'):
        dpg.add_spacer(height=10)
        with dpg.table(tag='summary',borders_outerH=True,borders_outerV=True,width=800,height=170,header_row=False,scrollY=True):
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text(temp["Summary"],wrap=750)

def stockpage():
    db = local_dh.SymbolGet()

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='stockpage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("stockpage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=410,callback=lambda: config.window_handler("stockpage",mainpage.mainpage,ui['g']))
            ui['b']['settings'] = dpg.add_button(label="Settings",width=410,callback=lambda: config.window_handler("stockpage",settingspage.settingspage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['stockname'] = dpg.add_text(db[stock])
        with dpg.group(tag='graph'):
            with dpg.plot(width=1250,height=400,anti_aliased=True):
                dpg.add_plot_axis(dpg.mvXAxis,tag='xaxis',time=True)
                dpg.add_plot_axis(dpg.mvYAxis,label="USD",tag='yaxis')
                multithread.run_parallel(graph_print)
        with dpg.group(tag="periods",horizontal=True,horizontal_spacing=5):
            dpg.add_button(label="1d",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"1d","1m"))
            dpg.add_button(label="5d",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"5d","1m"))
            dpg.add_button(label="1m",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"1mo","1d"))
            dpg.add_button(label="3m",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"3mo","1d"))
            dpg.add_button(label="6m",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"6mo","1d"))
            dpg.add_button(label="1y",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"1y","1d"))
            dpg.add_button(label="2y",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"2y","1d"))
            dpg.add_button(label="5y",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"5y","1d"))
            dpg.add_button(label="10y",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"10y","1d"))
            dpg.add_button(label="ytd",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"ytd","1d"))
            dpg.add_button(label="max",width=105,callback=lambda:multithread.run_parallel(graph_update,stock,"max","1d"))
        with dpg.group(tag='infotablegroup',horizontal=True):
            multithread.run_parallel(info_print)

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    ui['g'] += config.ui_center('graph',0)
    ui['g'] += config.ui_center('periods',0)
    ui['g'] += config.ui_center('infotablegroup',0)
    dpg.bind_item_font(ui['l']['stockname'],theme.font_registry.JBM[25])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
