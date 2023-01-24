import dearpygui.dearpygui as dpg
import config
import theme
import loginpage
import mainpage
import portfoliopage
import authentication
import local_dh

def changepwd(x):
    dpg.set_value(x['l']['pstatus'],"")
    oldp = dpg.get_value(x['i']["oldp"]).strip()
    p1 = dpg.get_value(x['i']["password1"]).strip()
    p2 = dpg.get_value(x['i']["password2"]).strip()
    if authentication.Decoder(authentication.curr_password) == oldp:
        if p1 != p2:
            dpg.set_value(x['l']['pstatus'],"Passwords Donot Match!")
        elif p1 == "":
            dpg.set_value(x['l']['pstatus'],"Invalid Passwords!")
        else:
            database = local_dh.ReadDB('DATABASE.DB')
            database['users'][authentication.curr_username] = authentication.Encoder(p1)
            local_dh.WriteDB(database,"DATABASE.DB")
            dpg.set_value(x['l']['pstatus'],"Password Updated Successfully!")
    else:
        dpg.set_value(x['l']['pstatus'],"Incorrect Password!")
        

def settingspage():

    ui = {"g":[], "l":{}, "b":{}, "i":{}}
    with dpg.group(tag='settingspage',parent='main'):
        with dpg.group(tag='topbar',horizontal=True,horizontal_spacing=5):
            ui['b']['logout'] = dpg.add_button(label="Logout",width=410,callback=lambda: config.window_handler("settingspage",loginpage.loginpage,ui['g']))
            ui['b']['mainpage'] = dpg.add_button(label="Mainpage",width=410,callback=lambda: config.window_handler("settingspage",mainpage.mainpage,ui['g']))
            ui['b']['portfolio'] = dpg.add_button(label="Portfolio",width=410,callback=lambda: config.window_handler("settingspage",portfoliopage.portfoliopage,ui['g']))
        with dpg.group(tag='title'):
            ui['l']['settings'] = dpg.add_text("Settings")
        with dpg.group(tag='changepwdprompt'):
            dpg.add_spacer(height=25)
            ui['l']['pchangelabel'] = dpg.add_text("Password Change",indent=80)
            with dpg.group(horizontal=True):
                ui["l"]["oldp"] = dpg.add_text("Old Password:")
                ui['i']['oldp'] = dpg.add_input_text(width=200,password=True)
            with dpg.group(horizontal=True):
                ui["l"]["password"] = dpg.add_text("New Password:")
                ui['i']['password1'] = dpg.add_input_text(width=200,password=True)
            with dpg.group(horizontal=True):
                ui["l"]["confirm_password"] = dpg.add_text("     Confirm:")
                ui['i']['password2'] = dpg.add_input_text(width=200,password=True)
            ui['b']['changepwd'] = dpg.add_button(label="Set",callback=lambda:changepwd(ui),width=335)
        with dpg.group(tag="pstatusgroup"):
            ui["l"]["pstatus"] = dpg.add_text("")

    ui['g'] += config.ui_center('topbar',0)
    ui['g'] += config.ui_center('title',0)
    ui['g'] += config.ui_center('changepwdprompt',0)
    ui['g'] += config.ui_center('pstatusgroup',0)
    dpg.bind_item_font(ui['l']['settings'],theme.font_registry.JBM[35])
    dpg.bind_item_font('topbar',theme.font_registry.JBM[25])
    dpg.bind_item_font(ui['l']['pchangelabel'],theme.font_registry.JBM[25])
