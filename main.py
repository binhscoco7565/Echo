# UI Libraries
import dearpygui.dearpygui as dpg
import art

# Admin stuff
import ctypes

# Import windows
from scripts.elevated import privacy, winutil, binds, backup_time
from scripts.normal import scoop, launch_priv, backup_user


dpg.create_context()


def is_admin():
    ctypes.windll.shell32.IsUserAnAdmin()


def main():
    # Defines options for window to open

    # Admin check using ctypes (Apparently not very secure...)
    if ctypes.windll.shell32.IsUserAnAdmin() == 1:
        print('Running in admin')
        with dpg.window(label='Echo (admin)', no_resize=True, no_title_bar=False) as main_window:
            # Title & VERY BAD padding (like wtf is this)
            dpg.add_text(f'{art.text2art('Echo', font='big')}')
            dpg.add_text('Admin enabled\n\n', color=(255, 0, 0))
            # Opens tree node aka "windows" in this context
            winutil.win_util()
            privacy.privacy()
            binds.binds()
            backup_time.backup_time()
    else:
        with dpg.window(label='Echo (non-admin)', no_resize=True, no_title_bar=False) as main_window:
            dpg.add_text(f'{art.text2art('Echo\n\n', font='big')}')
            scoop.scoop_window()
            launch_priv.launch_priv()
            backup_user.backup_user()

    dpg.create_viewport(title='Echo', width=700, height=800, min_width=600, min_height=250, decorated=True)
    dpg.setup_dearpygui()

    dpg.show_viewport(maximized=False)
    dpg.set_primary_window(main_window, True)

    dpg.start_dearpygui()


if __name__ == '__main__':
    main()
