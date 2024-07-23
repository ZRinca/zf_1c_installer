from design_core import InstallerWindow
import customtkinter as ctk


class RegistrationsOneC(InstallerWindow):
    header_text = 'Введите логин и пароль от вашей 1С.'
    body_text = '1С, которую вы выбрали, требует авторизации. Пожалуйста,введите логин и пароль.'

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['publish_1c', 'check_functionality', 'install_1c_extension']
        all_false = not all(not global_config[key] for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        login_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), placeholder_text="Логин",
                                   placeholder_text_color="grey")
        login_entry.pack(padx=24, pady=(24, 0), fill='x')

        password_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), show='*', placeholder_text="Пароль",
                                      placeholder_text_color="grey")
        password_entry.pack(padx=24, pady=(13, 24), fill='x')
