import subprocess
import tkinter.messagebox
import webbrowser

import dearpygui.dearpygui as dpg


def open_winutil():
    try:
        subprocess.call('powershell.exe -Command "iwr -useb https://christitus.com/win | iex"', shell=True)
    except PermissionError as e:
        tkinter.messagebox.showerror(title='Error', message=str(e))


def win_util():
    with dpg.tree_node(label='Chris Titus Tech\'s WinUtil'):
        with dpg.group(tag='winutil_group'):
            dpg.add_text(
                "Contains useful utilities and commands to slim down windows, reduce number of processes and make Windows generally better. Has been tested on Windows 10 and 11. ",
                wrap=0)

            with dpg.group(horizontal=True):
                dpg.add_button(label='Source',
                               callback=lambda: webbrowser.open('https://github.com/ChrisTitusTech/winutil'))
                dpg.add_button(label='Run', callback=open_winutil)

            # Absolutely disgusting way to make a margin
            dpg.add_text('\n')
