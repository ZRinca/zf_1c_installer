from design_core import InstallerWindow
import customtkinter as ctk


class RegistrationsOneC(InstallerWindow):
    header_text = 'Введите логин и пароль от вашей 1С.'
    body_text = "1С, которую вы выбрали, требует авторизации. Пожалуйста,введите логин и пароль."

    def draw(self):
        super().draw()

        login_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), placeholder_text="Логин",
                                   placeholder_text_color="grey")
        login_entry.pack(padx=24, pady=(24, 0), fill='x')

        password_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), show='*', placeholder_text="Пароль",
                                      placeholder_text_color="grey")
        password_entry.pack(padx=24, pady=(13, 24), fill='x')