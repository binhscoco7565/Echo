import dearpygui.dearpygui as dpg
import winreg
import tkinter.messagebox
import subprocess
import urllib.request as req
import os


def check_biometrics():
    # Opens PassportForWork key, which is one of the keys modified and checks if enabled
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r'Software\\Policies\\Microsoft\\PassportForWork\\')
        passport_enabled = winreg.QueryValueEx(key, 'Enabled')
    except FileNotFoundError:
        return 'not supported'
    return bool(passport_enabled)


def install():
    try:
        dpg.add_text(parent='binds_group', default_value='Installing...', color=(255, 255, 0, 255),
                     tag='registry')
        req.urlretrieve('https://raw.githubusercontent.com/binhscoco7565/Echo/master/assets/biometrics.reg',
                        '.')
        subprocess.call('powershell.exe -Command reg import ./biometrics.reg')
        subprocess.call('powershell.exe -Command rm ./biometrics.reg')
    except Exception as e:
        tkinter.messagebox.showerror('Error', str(e))

    dpg.delete_item('registry')


def backup_restore(operation):
    if operation == 'backup':
        dpg.add_text(parent='biometrics_group', default_value='Backing up...', color=(255, 255, 0, 255), tag='alert')
        subprocess.call(f"powershell.exe -Command reg export HKLM ./HKLM.reg.bak /y")
        subprocess.call(f"powershell.exe -Command reg export HKCU ./HKCU.reg.bak /y")
        tkinter.messagebox.showinfo(title="Complete", message="Backup complete")
        dpg.delete_item('alert')
    elif operation == 'restore':
        if os.path.exists(f'./HKLM.reg.bak'):
            dpg.add_text(parent='biometrics_group', default_value='Backing up...', color=(255, 255, 0, 255),
                         tag='alert')
            subprocess.call(f"powershell.exe -Command reg import ./HKLM.reg.bak")
            subprocess.call(f"powershell.exe -Command reg import ./HKCU.reg.bak")
            tkinter.messagebox.showinfo(title="Complete", message="Modifications made! Please reboot")
            dpg.delete_item('alert')
        else:
            tkinter.messagebox.showwarning(title="Warning!",
                                           message="Modifications NOT made! Has a registry backup been provided?")


def biometrics():
    with dpg.tree_node(label='Enabling biometrics on enterprise devices'):
        with dpg.group(tag='biometrics_group'):
            dpg.add_text(
                'Uses group policy edits through the registry editor to enable biometrics on enterprise devices that have it disabled. NOTE: While this has been tested on work laptops before, unintended effects on networking, domain accounts and other issues may come up. Use with caution and always back up registry beforehand.',
                wrap=0)
            dpg.add_text(f'Biometrics enabled: {str(check_biometrics()).lower()}')

        with dpg.group(tag='biometrics_buttons', horizontal=True):
            dpg.add_button(label='Backup registry', callback=lambda: backup_restore('backup'))
            dpg.add_button(label='Enable biometrics')
            dpg.add_button(label='Restore registry', callback=lambda: backup_restore('restore'))
