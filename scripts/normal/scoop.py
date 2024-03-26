import dearpygui.dearpygui as dpg
import tkinter.messagebox
import webbrowser
import subprocess
import os

scoop_path = f'C:\\Users\\{os.getlogin()}\\scoop'


def install():
    # We need to use .Popen since the scoop install script doesn't currently have return codes.
    dpg.add_text(parent='scoop_group', default_value='Installing...', color=(255, 255, 0, 255), tag='installing')
    proc = subprocess.Popen('powershell.exe -Command irm get.scoop.sh | iex', stdout=subprocess.PIPE)
    output = proc.stdout.read()
    try:
        if 'already installed' in str(output):
            raise Exception('Scoop already installed')
        else:
            tkinter.messagebox.showinfo('Info', 'Install complete')
    except Exception as e:
        tkinter.messagebox.showerror('Error', str(e))

    dpg.delete_item('installing')


def uninstall():
    if os.path.exists(scoop_path):
        proc = subprocess.Popen('powershell.exe -Command scoop uninstall scoop', stdout=subprocess.PIPE)
        output = proc.stdout.read()
        try:
            if 'failed' in str(output):
                raise Exception('Unable to uninstall scoop. Please check scoop\'s website')
            else:
                tkinter.messagebox.showinfo('Info', 'Uninstall complete')
        except Exception as e:
            tkinter.messagebox.showerror('Error', str(e))


def scoop_window():
    with dpg.tree_node(label='Install Scoop package manager'):
        with dpg.group(tag='scoop_group'):
            dpg.add_text(
                'Download and Install the Scoop.sh package manager. Very useful command-line utility to remove the need for manually downloading and installing portable applications. From utilities such as MSEdgeRedirect to restricted apps such as the Official Minecraft Launcher, a large number of applications can be acquired using scoop.',
                wrap=0)

        with dpg.group(tag='scoop_group_buttons', horizontal=True):
            dpg.add_button(label='Source', callback=lambda: webbrowser.open('https://scoop.sh'))
            dpg.add_button(label='Install', callback=install)
            dpg.add_button(label='Uninstall', callback=uninstall)
