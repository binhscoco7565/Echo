# UI Libraries
import dearpygui.dearpygui as dpg
import art

# Admin stuff
import ctypes
import argparse

# Import windows
from scripts.elevated import privacy, winutil, binds, backup_time, biometrics_enterprise
from scripts.normal import scoop, launch_priv, backup_user, binds_non

# Import platform status & checks
import status

dpg.create_context()

# Process and set conditions for arguments
parser = argparse.ArgumentParser(description='Echo utility for windows')
parser.add_argument('--non-admin', help='Forces app to run as unprivileged user. Will override --force-admin',
                    action=argparse.BooleanOptionalAction)
parser.add_argument('--force-admin', help='Forces app to run as admin in unprivileged users (not recommended)',
                    action=argparse.BooleanOptionalAction)
args = vars(parser.parse_args())


def main():
    # Defines options for window to open

    # Admin check using ctypes (Apparently not very secure...) + checking arguments to launch correct version
    if (ctypes.windll.shell32.IsUserAnAdmin() == 1 or args['force_admin']) and not args['non_admin']:
        print('Running in admin')
        with dpg.window(label='Echo (admin)', no_resize=True, no_title_bar=False) as main_window:
            # Title & VERY BAD padding (like wtf is this)
            dpg.add_text(art.text2art('Echo', font='big'))
            status.status('enabled')

            dpg.add_text('\n')
            # Opens tree node aka "windows" in this context
            winutil.win_util()
            biometrics_enterprise.biometrics()
            binds.binds()
            # backup_time.backup_time()
            # privacy.privacy()
    else:
        with dpg.window(label='Echo (non-admin)', no_resize=True, no_title_bar=False) as main_window:
            dpg.add_text(art.text2art('Echo', font='big'))
            status.status('disabled')

            dpg.add_text('\n')

            scoop.scoop_window()
            launch_priv.launch_priv()
            backup_user.backup_user()
            binds_non.binds_non()

    dpg.create_viewport(title='Echo', width=700, height=800, min_width=600, min_height=250, decorated=True)
    dpg.setup_dearpygui()

    dpg.show_viewport(maximized=False)
    dpg.set_primary_window(main_window, True)

    dpg.start_dearpygui()


if __name__ == '__main__':
    main()
