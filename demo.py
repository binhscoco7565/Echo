import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import datetime
import glob
import os

import ctypes


def window():
    dpg.create_context()
    dpg.create_viewport(title='Custom Title', width=600, height=600)

    demo.show_demo()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == '__main__':
    window()
