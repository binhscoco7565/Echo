import dearpygui.dearpygui as dpg
import webbrowser

def install_scoop():
    return


def scoop_window():
    with dpg.tree_node(label='Install Scoop package manager'):
        with dpg.group(tag='scoop_group'):
            dpg.add_text(
                'Download and Install the Scoop.sh package manager. Very useful command-line utility to remove the need for manually downloading and installing portable applications. From utilities such as MSEdgeRedirect to restricted apps such as the Official Minecraft Launcher, a large number of applications can be acquired using scoop.',
                wrap=0)

            # amazing margin
            dpg.add_text('\n')
            with dpg.group(tag='scoop_group_buttons', horizontal=True):
                dpg.add_button(label='Source', callback=lambda: webbrowser.open('https://scoop.sh'))
                dpg.add_button(label='Install/Uninstall')
