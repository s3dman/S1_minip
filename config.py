import dearpygui.dearpygui as dpg

W,H = 1280,720
counter = 0

def window_handler(wdt,wcf,hr):
    for i in hr:
        dpg.set_item_callback(i,lambda: None)
    dpg.delete_item(wdt)
    wcf()

def ui_center(item, alignment_type: int, x_align: float = 0.5, y_align: float = 0.5):
    def _center_h(_s, _d, data):
        width = dpg.get_item_rect_size(data[0])[0]
        newX = (W // 2 - width // 2) * data[1] * 2
        dpg.set_item_pos(data[0], [newX, dpg.get_item_pos(data[0])[1]])

    def _center_v(_s, _d, data):
        height = dpg.get_item_rect_size(data[0])[1]
        newY = (H // 2 - height // 2) * data[1] * 2
        dpg.set_item_pos(data[0], [dpg.get_item_pos(data[0])[0], newY])

    if 0 <= alignment_type <= 2:
        with dpg.item_handler_registry() as a:
            if alignment_type == 0:
                # horizontal only alignment
                dpg.add_item_visible_handler(callback=_center_h, user_data=[item, x_align])
            elif alignment_type == 1:
                # vertical only alignment
                dpg.add_item_visible_handler(callback=_center_v, user_data=[item, y_align])
            elif alignment_type == 2:
                # both horizontal and vertical alignment
                dpg.add_item_visible_handler(callback=_center_h, user_data=[item, x_align])
                dpg.add_item_visible_handler(callback=_center_v, user_data=[item, y_align])
        dpg.bind_item_handler_registry(item, dpg.last_container())
        return dpg.get_item_children(a,slot=1)
