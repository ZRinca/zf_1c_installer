from design_core import InstallerWindow


class GoodByeWindow(InstallerWindow):

    header_text = 'Установка завершена'
    body_text = 'Установка завершена, и Zero Factor установлен. Спасибо, что выбрали нас!'

    draw_next_button = False
    draw_back_button = False
