import os

import dearpygui.dearpygui as dpg


def run_priv():
    path = dpg.get_value('input')
    print(path)
    os.popen(f'cmd.exe /min /C \"set __COMPAT_LAYER=RUNASINVOKER && {path}')


# Launches escalated application without the need for admin (Has like a 10% chance of working on installers)
def backup_time():
    with dpg.tree_node(label='Routine home folder backups'):
        with dpg.group(label='launch_priv_group'):
            dpg.add_text(
                'Implements regular backups for Documents, Pictures, Downloads and etc. Uses task scheduler and custom batch scripts to run at specified time intervals. Options are also available to automatically delete very old backups.',
                wrap=0)
            dpg.add_input_text(tag='custom_path', label='Custom Path (Works with cloud e.g. OneDrive)', width=300)
            # Combo for interval
            dpg.add_combo(('Daily', 'Weekly', 'Monthly'), tag='interval', width=200)
            # Sliders for options
            dpg.add_slider_int(label='Max no. of backups before deletion (0 defaults to 10)', tag='max_backups',
                               width=200, max_value=30)
            dpg.add_slider_int(label='Time of day to perform backup', tag='time', width=200, max_value=24)
            dpg.add_button(label='Save settings', callback=lambda: run_priv())
