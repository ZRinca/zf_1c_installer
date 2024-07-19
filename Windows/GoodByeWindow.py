from design_core import InstallerWindow
import customtkinter as ctk


class GoodByeWindow(InstallerWindow):

    header_text = 'Прощайте!'
    body_text = 'При нажатии на кнопку «Далее» вы принимаете условия лицензионного соглашения'

    draw_next_button = False
    # draw_back_button = False
