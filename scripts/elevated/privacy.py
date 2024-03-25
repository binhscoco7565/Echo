import dearpygui.dearpygui as dpg


def privacy():
    with dpg.tree_node(label='Install and run privacy.sexy'):
        with dpg.group(tag='privacy_group'):
            dpg.add_text('test')
            dpg.add_button(label='test')

        # Here it is again...
        dpg.add_text('\n')
