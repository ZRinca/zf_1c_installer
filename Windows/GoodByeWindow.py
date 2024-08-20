from design_core import InstallerWindow


class GoodByeWindow(InstallerWindow):

    header_text = 'Завершение установки'
    body_text = 'Установка завершена. Спасибо, что выбрали нас!'

    draw_next_button = False
    draw_back_button = False
