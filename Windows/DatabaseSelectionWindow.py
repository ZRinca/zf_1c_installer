from design_core import InstallerWindow
import customtkinter as ctk


class DataBaseSelection(InstallerWindow):
    header_text = "Выберите базу из списка"
    body_text = "Программа нашла на вашем устройстве несколько установленных баз.В списке ниже указаны все\nустановленныебазы 1С."

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_1c_extension', 'publish_1c', 'connect_database', 'check_functionality']
        all_false = not all(not global_config[key] for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()
        database_combobox = ctk.CTkComboBox(self.main_frame, variable=None, values=None,
                                            font=("Rubik Light", 12),
                                            state="readonly", border_color='#B3B7B1', button_color="#B3B7B1")
        database_combobox.pack(padx=24, pady=24, fill='x')

