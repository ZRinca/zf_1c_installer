from design_core import InstallerWindow
import customtkinter as ctk


class OneCSelection(InstallerWindow):
    header_text = "Выберите 1C из списка", "Программа нашла на вашем устройстве "
    body_text = ("Программа нашла на вашем устройстве несколько установленных 1С.В списке ниже указаны все "
                 "установленные версии 1С.")

    def draw(self):
        super().draw()
        database_combobox = ctk.CTkComboBox(self.main_frame, variable=None, values=None,
                                            font=("Rubik Light", 12),
                                            state="readonly", border_color='#B3B7B1', button_color="#B3B7B1")
        database_combobox.pack(padx=24, pady=24, fill='x')
