import dearpygui.dearpygui as dpg
import config
import theme
import local_dh
from difflib import SequenceMatcher
import loginpage 
import stockpage
import settingspage
import portfoliopage


ui = {"g":[], "l":{}, "b":{}, "i":{}}

def mainpage():

    db = local_dh.SymbolGet().items()

    def tablesearch():
        dpg.delete_item(item="stocktable",children_only=True)
        val = dpg.get_value(ui['i']['searchbar'])

        if val == "":
            temp_db = db
        else:
            similar = []
            for i in db:
                if SequenceMatcher(None,val.lower(),i[1].lower()).ratio() >= 0.5 or val.lower() == i[0].lower():
                    similar.append(i)
            temp_db=similar
        dpg.add_table_column(parent='stocktable')
        if len(temp_db) == 0:
            with dpg.table_row(parent='stocktable'):
                dpg.add_text("No results found!")
        else:
            for i in temp_db:
                with dpg.table_row(parent='stocktable'):
                    ui['b'][i[0]] = dpg.add_button(label=f"{i[0]} : {i[1]}",width=1000,callback=stockpage.page_handler)


    with dpg.group(tag='mainpage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("mainpage",loginpage.loginpage,ui['g']))
            ui['b']['portfolio'] = dpg.add_button(label="Portfolio",width=410,callback=lambda: config.window_handler("mainpage",portfoliopage.portfoliopage,ui['g']))
            ui['b']['settings'] = dpg.add_button(label="Settings",width=410,callback=lambda: config.window_handler("mainpage",settingspage.settingspage,ui['g']))

        with dpg.group(tag='searchbar'):
            ui['i']['searchbar'] = dpg.add_input_text(hint="Search:",width=500,on_enter=True,callback=tablesearch)
        with dpg.group(tag='stocktablegroup'):
            with dpg.table(tag='stocktable',borders_outerH=True,borders_outerV=True,width=1000,height=550,header_row=False,scrollY=True):
                tablesearch()
        ui['g'] += config.ui_center('topbar',0)
        ui['g'] += config.ui_center('searchbar',2,y_align=0.1)
        ui['g'] += config.ui_center('stocktablegroup',2,y_align=0.7)
        dpg.bind_item_font(ui['i']['searchbar'],theme.font_registry.JBM[25])
        dpg.bind_item_font('topbar',theme.font_registry.JBM[25])