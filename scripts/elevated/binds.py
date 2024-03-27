import os
import tkinter.messagebox
import urllib.request as req

import dearpygui.dearpygui as dpg

bind_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\shortcuts.ahk'


def binds():
    # Checks which operation is being done and return the correct state for each
    def check_installed():
        return os.path.exists(bind_path)

    def shortcut_operate(operation, user_data):
        if operation:
            try:
                dpg.add_text(parent='binds_group', default_value='Installing...', color=(255, 255, 0, 255),
                             tag='installing')
                req.urlretrieve('https://raw.githubusercontent.com/binhscoco7565/Echo/master/assets/binds.ahk',
                                bind_path)
            except PermissionError as e:
                tkinter.messagebox.showerror(title='Error', message=str(e))
        else:
            try:
                os.remove(bind_path)
            except FileNotFoundError as e:
                tkinter.messagebox.showerror(title='Error', message=str(e))

        dpg.delete_item('installing')
        dpg.configure_item('install_text', default_value=f'Installed: {str(check_installed()).lower()}')

    installed = check_installed()

    with dpg.tree_node(label='Fetch and run suggested AHK binds (For all users)'):
        with dpg.group(tag='binds_group'):
            dpg.add_text('Download Binds that help with faster typing & makes stuff looks nicer. A few binds include:',
                         wrap=0)
            dpg.add_text('dlt -> Δ', bullet=True)
            dpg.add_text('dgr -> °', bullet=True)
            dpg.add_text('          ... plus more')
            installed_text = dpg.add_text(f'Installed: {str(installed).lower()}')
            # Don't know why I'm doing this, logic doesn't make sense
            with dpg.group(horizontal=True):
                dpg.add_button(label='Source')
                dpg.add_button(label='Download and make run on startup',
                               callback=lambda: shortcut_operate(True, installed_text), user_data=installed_text)
                dpg.add_button(label='Remove', callback=lambda: shortcut_operate(False, installed_text),
                               user_data=installed_text)

            # Just when I thought it was gone
            dpg.add_text('\n')
