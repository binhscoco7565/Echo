import dearpygui.dearpygui as dpg
import os


def run_priv():
    path = dpg.get_value('input')
    print(path)
    os.popen(f'cmd.exe /min /C \"set __COMPAT_LAYER=RUNASINVOKER && {path}')


# Launches escalated application without the need for admin (Has like a 10% chance of working on installers)
def launch_priv():
    with dpg.tree_node(label='Launch executable as \'admin\' (Doesn\'t work 95% of the time)'):
        with dpg.group(label='launch_priv_group'):
            dpg.add_text(
                'Attempts to launch an app as admin using some quirky methods. This \'hack\' will have a 95% chance of not working whatsoever, but it is still possible for an application to continue. Adds right-click menu options (context menu) for running an admin application as a non-escalated user. If running an installer using this method, change the installation directory to one that the user owns. Probably less convenient than creating a batch script, but easier for inexperienced users.',
                wrap=0)
            dpg.add_input_text(hint='Paste in path to executable', tag='input')
            dpg.add_button(label='Run', callback=lambda: run_priv())
