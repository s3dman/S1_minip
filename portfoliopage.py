import dearpygui.dearpygui as dpg
import config
import theme
import loginpage
import mainpage
import settingspage
import authentication
import local_dh
import data_fetch
import multithread

pW,pH = 500,200
stocklist = local_dh.SymbolGet()
def add_investment():
    ui = {"g":[], "l":{}, "b":{}, "i":{}}

    def pricefetch(pset=True):
        if dpg.get_value(ui['i']['stockname']) in stocklist:
            dpg.set_value(ui['l']['status_info'],"")
            if pset:
                dpg.set_value(ui['i']['price'],
                    data_fetch.stock_info(dpg.get_value(ui['i']['stockname']))["Current Price"][1:],False)
            return 0
        dpg.set_value(ui['l']['status_info'],"Invalid Stock!")
        return -1

    def qtyupdate(f):
        d = dpg.get_value(ui['i']['qty'])
        if d == "":
            dpg.set_value(ui['i']['qty'],1)
        else:
            d = int(float(d))
            if f>0:
                dpg.set_value(ui['i']['qty'],d+f)
            elif d>1:
                dpg.set_value(ui['i']['qty'],d+f)
            else:
                dpg.set_value(ui['i']['qty'],1)

    def add_stock():
        qtyupdate(0)
        qty = dpg.get_value(ui['i']['qty'])
        if pricefetch(pset=False) == 0:
            user_data = local_dh.userDataRead(authentication.curr_username)
            stockname = dpg.get_value(ui['i']['stockname'])
            price = dpg.get_value(ui['i']['price']) 
            if price == "" or int(float(price)) == 0:
                pricefetch()
            price = dpg.get_value(ui['i']['price']) 
            user_data.append([stockname,int(qty),float(price)])
            local_dh.userDataWrite(authentication.curr_username,user_data)
            config.window_handler("popup",None,ui['g'],popup=True)
            multithread.run_parallel(table_update)
            multithread.run_parallel(graphupdate)

    with dpg.window(tag='popup',width=pW,height=pH,pos=(int(config.W/2-pW/2),int(config.H/2-pH/2)),no_collapse=True,no_move=True,no_title_bar=True,modal=True):
        dpg.add_spacer(height=7)
        with dpg.group(tag='titlegroup'):
            ui['l']['investment_title'] = dpg.add_text("Add Investment")
        dpg.add_spacer(height=7)
        with dpg.group(tag='popupgroup'):
            with dpg.group(tag='stock',horizontal=True):
                ui['i']['stockname'] = dpg.add_input_text(uppercase=True,hint="Stock",width=200)
                ui['l']['status_info'] = dpg.add_text()
                # ui['b']['stockcheck'] = dpg.add_button(label="Fetch",width=200,callback=stockcheck)
            with dpg.group(tag='qty',horizontal=True):
                ui['i']['qty'] = dpg.add_input_text(hint="Quantity",width=200,decimal=True)
                ui['b']['qtyp'] = dpg.add_button(label="+",callback=lambda:qtyupdate(1))
                ui['b']['qtym'] = dpg.add_button(label="-",callback=lambda:qtyupdate(-1))
            with dpg.group(tag='price',horizontal=True):
                ui['i']['price'] = dpg.add_input_text(hint='Buy Price',width=200,decimal=True)
                ui['b']['pricecheck'] = dpg.add_button(label="Get Current Price",width=200,callback=pricefetch)
            with dpg.group(tag='buttons',horizontal=True,horizontal_spacing=208):
                ui['b']['cancel'] = dpg.add_button(label="Cancel",width=100,callback=lambda:config.window_handler("popup",None,ui['g'],popup=True))
                ui['b']['add'] = dpg.add_button(label="Add",width=100,callback=add_stock)
    ui['g'] += config.ui_center('titlegroup',0,W=500,H=250)
    ui['g'] += config.ui_center('popupgroup',0,W=500,H=250)

def graphupdate():
    user_data = local_dh.userDataRead(authentication.curr_username)
    if len(user_data) == 0:
        return -1
    date,open,high,low,close = data_fetch.stock_history_period(user_data[0][0],"6mo","1d")
    for k in range(len(date)):
        open[k] = int(open[k])*user_data[0][1]
        high[k] *= int(high[k])*user_data[0][1]
        low[k] *= int(low[k])*user_data[0][1]
        close[k] *= int(close[k])*user_data[0][1]
    for i in user_data[1:]:
        t_open,t_high,t_low,t_close = data_fetch.stock_history_period(i[0],"6mo","1d",dateget=False)
        for j in range(len(date)):
            open[j] += int(t_open[j])*i[1]
            high[j] += int(t_high[j])*i[1]
            low[j] += int(t_low[j])*i[1]
            close[j] += int(t_close[j])*i[1]
    for k in range(len(close)):
        close[k] /= 1e6

    dpg.set_value('series',(date,close))
    dpg.set_axis_limits_auto('xaxis')
    dpg.set_axis_limits('xaxis',ymax=date[-1],ymin=date[0])
    dpg.fit_axis_data('yaxis')

def overallinfoupdate(ui):
    user_data = local_dh.userDataRead(authentication.curr_username)
    if len(user_data) == 0:
        return -1
    bprice,cprice,pcprice = 0,0,0
    for i in user_data:
        df = data_fetch.stock_info(i[0],False)
        cprice += float(df["Current Price"][1:])*i[1]
        pcprice += float(df["Previous Close"][1:])*i[1]
        bprice += i[1]*i[2]
    dgainp,tgainp = cprice-pcprice,cprice-bprice

    # dcolor,tcolor = [0,255,0],[0,255,0]
    # if dgainp<0:
    #     dcolor = [255,0,0]
    # if tgainp<0:
    #     tcolor = [255,0,0]

    dpg.set_value(ui['l']['daygain'],f"Day Gain/Loss: {dgainp:.3f}$ ({dgainp/bprice*100:.3f}%)")
    dpg.set_value(ui['l']['totalgain'],f"Total Gain/Loss: {tgainp:.3f}$ ({tgainp/bprice*100:.3f}%)")
    dpg.set_value(ui['l']['numinvestments'],f"Investment's: {len(user_data)}")

def delete_investment(source):
    user_data = local_dh.userDataRead(authentication.curr_username)
    index = dpg.get_item_user_data(source)
    del user_data[index]
    local_dh.userDataWrite(authentication.curr_username,user_data)
    multithread.run_parallel(table_update)
    multithread.run_parallel(graphupdate)

def table_update():
    dpg.delete_item('investmenttable',children_only=True)
    dpg.add_table_column(parent='investmenttable',label="Stock")
    dpg.add_table_column(parent='investmenttable',label="Quantity")
    dpg.add_table_column(parent='investmenttable',label="Buy Price")
    dpg.add_table_column(parent='investmenttable',label="",width=2,width_fixed=True)
    user_data = local_dh.userDataRead(authentication.curr_username)
    for i in range(len(user_data)):
        with dpg.table_row(parent='investmenttable'):
            for j in range(4):
                with dpg.table_cell():
                    if j == 2:
                        dpg.add_text(f"${user_data[i][j]}")
                    elif j == 3:
                        dpg.add_button(label=f"-",user_data=i,callback=delete_investment)
                    else:
                        dpg.add_text(user_data[i][j])



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
                dpg.add_plot_axis(dpg.mvYAxis,label="USD (Mil)",tag='yaxis')
                dpg.add_line_series(x=[],y=[],parent='yaxis',tag='series')
                multithread.run_parallel(graphupdate)
        with dpg.group(tag='overallinfo',pos=(100,520)):
            ui['l']['daygain'] = dpg.add_text("Day Gain:",color=[255,255,255])
            ui['l']['totalgain'] = dpg.add_text("Total Gain:",color=[255,255,255])
            ui['l']['numinvestments'] = dpg.add_text("Invesments:")
            dpg.add_spacer(height=20)
            ui['b']['addinvestment'] = dpg.add_button(label="Add Investment",width=200,callback=add_investment)
            multithread.run_parallel(overallinfoupdate,ui)
        with dpg.group(tag='investment',pos=(600,520)):
            with dpg.table(tag='investmenttable',borders_outerH=True,borders_outerV=True,width=600,height=150,header_row=True,scrollY=True):
                table_update()

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    ui['g'] += config.ui_center('graph',0)
    dpg.bind_item_font(ui['l']['portfolio'],theme.font_registry.JBM[30])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
    dpg.bind_item_font(ui['b']['addinvestment'],theme.font_registry.JBM[25])
