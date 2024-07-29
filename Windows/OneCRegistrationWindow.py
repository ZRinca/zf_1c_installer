from design_core import InstallerWindow
import customtkinter as ctk


class RegistrationsOneC(InstallerWindow):
    header_text = 'Введите логин и пароль от вашей 1С.'
    body_text = '1С, которую вы выбрали, требует авторизации. Пожалуйста,введите логин и пароль.'

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['publish_1c', 'check_functionality', 'install_1c_extension']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        self.login_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), placeholder_text="Логин",
                                        placeholder_text_color="grey")
        self.login_entry.pack(padx=24, pady=(24, 0), fill='x')

        self.password_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), show='*', placeholder_text="Пароль",
                                           placeholder_text_color="grey")
        self.password_entry.pack(padx=24, pady=(13, 24), fill='x')

        self.login_entry.bind("<KeyRelease>", lambda _: self.update_login())
        self.password_entry.bind("<KeyRelease>", lambda _: self.update_password())

    def update_login(self):
        login = self.login_entry.get()
        self.global_config['LOGIN'] = login

    def update_password(self):
        password = self.password_entry.get()
        self.global_config['PASSWORD'] = password