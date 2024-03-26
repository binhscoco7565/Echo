import os
import tkinter.messagebox
import urllib.error
import urllib.request as req

import dearpygui.dearpygui as dpg

# Basically the exact same version as the elevated binds_non.py, but this time is user-specific
bind_path = f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\binds.ahk'


def binds_non():
    # Checks which operation is being done and return the correct state for each
    def check_installed():
        if os.path.exists(bind_path):
            return True
        else:
            return False

    def shortcut_operate(operation):
        if operation:
            try:
                dpg.add_text(parent='binds_group', default_value='Installing...', color=(255, 255, 0, 255),
                             tag='installing')
                req.urlretrieve('https://raw.githubusercontent.com/binhscoco7565/Echo/master/assets/binds.ahk',
                                bind_path)
            except urllib.error.URLError or urllib.error.HTTPError or PermissionError as e:
                tkinter.messagebox.showerror('Error', e)
        else:
            try:
                os.remove(bind_path)
            except FileNotFoundError as e:
                tkinter.messagebox.showerror('Error', e)

        dpg.delete_item('installing')
        dpg.configure_item('install_text', default_value=f'Installed: {str(check_installed()).lower()}')

    with dpg.tree_node(label='Fetch and run suggested AHK binds (Only for current user)'):
        with dpg.group(tag='binds_group'):
            dpg.add_text('Download Binds that help with faster typing & makes stuff looks nicer. A few binds include:',
                         wrap=0)
            dpg.add_text('dlt -> Δ', bullet=True)
            dpg.add_text('dgr -> °', bullet=True)
            dpg.add_text('          ... plus more')

            # Shortcut already installed or not
            installed_text = dpg.add_text(f'Installed: {str(check_installed()).lower()}', tag='install_text')
            # Don't know why I'm doing this, logic doesn't make sense

        with dpg.group(horizontal=True):
            dpg.add_button(label='Source')
            dpg.add_button(label='Download and make run on startup',
                           callback=lambda: shortcut_operate(True))
            dpg.add_button(label='Remove', callback=lambda: shortcut_operate(False))
