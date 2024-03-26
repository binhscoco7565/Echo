import platform
import dearpygui.dearpygui as dpg


def status(admin):
    if admin == 'enabled':
        color = (255, 0, 0, 255)
    else:
        color = (255, 255, 255, 255)
    with dpg.group(tag='platform'):
        dpg.add_text(
            f'Platform: {platform.platform()}\nProcessor: {platform.processor()}\nVersion: {platform.version()}')

        with dpg.group(tag='admin', horizontal=True):
            dpg.add_text('Admin:')
            dpg.add_text(default_value=admin, color=color)
