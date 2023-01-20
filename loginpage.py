import dearpygui.dearpygui as dpg
import config
import theme
import authentication
import time

import mainpage

def loginpage():
    ui = {"g":[], "l":{}, "b":{}, "i":{}}

    def login_parser():
        dpg.delete_item('parser_out',children_only=True)
        c = authentication.Login(dpg.get_value(ui['i']['username']).strip(),
                                dpg.get_value(ui['i']['password']).strip())
        if c == 0:
            config.window_handler("loginpage",mainpage.mainpage,ui['g'])
        elif c == -1:
            ui['l']['wrong_pass'] = dpg.add_text("Invalid password!",parent='parser_out')
        elif c == -2:
            ui['l']['no_user'] = dpg.add_text("No user exists!",parent='parser_out')

    with dpg.group(tag='loginpage',parent='main'):

        with dpg.group(tag='login_prompt'):
            with dpg.group(horizontal=True):
                ui["l"]["username"] = dpg.add_text("Username:")
                ui['i']['username'] = dpg.add_input_text(width=200)
            with dpg.group(horizontal=True):
                ui["l"]["password"] = dpg.add_text("Password:")
                ui['i']['password'] = dpg.add_input_text(width=200,password=True)
        with dpg.group(tag='login_register_buttons',horizontal=True):
            ui["b"]["register"] = dpg.add_button(label="Register",width=100,height=50,
                callback=lambda: config.window_handler("loginpage",registerpage,ui['g']))
            ui["b"]["login"] = dpg.add_button(label="Login",width=100,height=50,
                                              callback=login_parser)
        with dpg.group(tag='parser_out'):
            pass

        ui['g'] += config.ui_center('login_prompt',2,0.5,0.45)
        ui['g'] += config.ui_center('login_register_buttons',2,0.5,0.55)
        ui['g'] += config.ui_center('parser_out',2,0.5,0.61)

def registerpage():
    ui = {"g":[], "l":{}, "b":{}, "i":{}}

    def register_parser():
        dpg.delete_item('parser_out',children_only=True)

        if dpg.get_value(ui['i']['username']) != "" and dpg.get_value(ui['i']['password1']) == dpg.get_value(ui['i']['password2']) and dpg.get_value(ui['i']['password1']) != "":

            c = authentication.Register(dpg.get_value(ui['i']['username']).strip(),
                                    dpg.get_value(ui['i']['password1']).strip())
            if c == 0:
                ui['l']['register_pass'] = dpg.add_text("Successfully registered!",parent='parser_out')
            else:
                ui['l']['already_registered'] = dpg.add_text("Already registered!",parent='parser_out')
        else:
            ui['l']['invalid_pass'] = dpg.add_text("Invalid username/passwords!",parent='parser_out')

    with dpg.group(tag='registerpage',parent='main'):

        with dpg.group(tag='register_prompt'):
            with dpg.group(horizontal=True):
                ui["l"]["username"] = dpg.add_text("Username:")
                ui['i']['username'] = dpg.add_input_text(width=200)
            with dpg.group(horizontal=True):
                ui["l"]["password"] = dpg.add_text("Password:")
                ui['i']['password1'] = dpg.add_input_text(width=200,password=True)
            with dpg.group(horizontal=True):
                ui["l"]["confirm_password"] = dpg.add_text(" Confirm:")
                ui['i']['password2'] = dpg.add_input_text(width=200,password=True)
        with dpg.group(tag='parser_out'):
            pass
        with dpg.group(tag='lr_buttons'):
            ui["b"]["register"] = dpg.add_button(label="Register",width=120,height=50,
                                                 callback=register_parser)
            ui["b"]["loginpage"] = dpg.add_button(label="Loginpage",width=120,height=50,
                callback=lambda: config.window_handler("registerpage",loginpage,ui['g']))

        ui['g'] += config.ui_center('register_prompt',2,0.4,0.5)
        ui['g'] += config.ui_center('lr_buttons',2,0.6,0.5)
        ui['g'] += config.ui_center('parser_out',2,0.5,0.6)

