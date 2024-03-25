import dearpygui.dearpygui as dpg
import tkinter.messagebox
import glob
import subprocess
import datetime
import os

# Initialise variables (NOTE: Somehow, variables have a few issues with dearpygui.
# They refuse to be persistent, and so using arguments into functions is the only way)
home = f'C:\\Users\\{os.getlogin()}\\'
onedrive_work_path = glob.glob(f'{home}OneDrive -*')[0]
custom_path = ''

custom_path_used = False
backup_folder_name = f'backups-{datetime.date.today()}\\'

# Future: Try to implement folder selection for backups, through listbox or checkbox. For now, these 2 folders will be backed up
copied_folders = ['Downloads', 'Pictures']

"""
This script uses xcopy to copy folders recursively and includes hidden + system file in its process. Arguments used taken from "xcopy /?"
/V - Verifies the size of each new file.
/Y - Suppresses prompting to confirm you want to overwrite an existing destination file.
/F - Displays full source and destination file names while copying.
/E - Copies directories and subdirectories, including empty ones.
/H - Copies hidden and system files also.
/I -  If destination does not exist and copying more than one file, assumes that destination must be a directory.
 
"""


def backup(option, custom_path=None):
    dpg.add_text(parent='backup_user_group', default_value='Copying...', tag='backup_alert', color=(255, 255, 0, 255))
    # Checks if custom path exists and is it actually selected
    if option == "Custom path (Double check Path!)" or not option:
        if not copied_folders:
            tkinter.messagebox.showinfo('Alert', 'No folders provided. No operation done')
        else:
            for folder in copied_folders:
                if not os.path.exists(f'{custom_path}{backup_folder_name}{folder}'):
                    os.makedirs(f'{custom_path}{backup_folder_name}{folder}')
                subprocess.call(
                    f'cmd.exe /C xcopy "{home}{folder}" "{custom_path}{backup_folder_name}{folder}" /VYFEHI',
                    shell=True)
            tkinter.messagebox.showinfo('Complete', f'Backup complete')
    # If none of those conditions are met, use OneDrive work
    else:
        if option == 'Personal Onedrive':
            onedrive_work_path = f'C:\\Users\\{os.getlogin()}\\OneDrive'
        for folder in copied_folders:
            if not os.path.exists(f'{onedrive_work_path}\\{backup_folder_name}{folder}'):
                os.makedirs(f'{onedrive_work_path}\\{backup_folder_name}{folder}')
            subprocess.call(
                f'cmd.exe /C xcopy "{home}{folder}" "{onedrive_work_path}\\{backup_folder_name}{folder}" /VYFEHI',
                shell=True)
        tkinter.messagebox.showinfo('Complete', f'Backup complete')

    dpg.delete_item('backup_alert')


# Backs up user folder (Doesn't include scheduling YET)
def backup_user():
    with dpg.tree_node(label='Backup important user folders'):
        with dpg.group(tag='backup_user_group'):
            dpg.add_text(
                'Saves important user folders to different sources of media. These folders include Documents, Downloads and Pictures. Backup destinations can be configured',
                wrap=0)
            dpg.add_combo(('Personal Onedrive', 'Onedrive for Work and School', 'Custom path (Double check Path!)'),
                          tag='combo')
            dpg.add_input_text(label='Custom Path', tag='custom_path')
        with dpg.group(horizontal=True):
            dpg.add_button(label='Backup',
                           callback=lambda: backup(dpg.get_value('combo'), dpg.get_value('custom_path')))
