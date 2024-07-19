from design_core import InstallerWindow
import customtkinter as ctk


class CustomiserWindow(InstallerWindow):
    header_text = 'Выбор компонентов'
    body_text = 'Выберите компоненты для установки'

    @classmethod
    def can_draw(cls, global_config):
        return global_config.get("custom_mode", False)

    def draw(self):
        super().draw()

        def checkbox_event():
            print(check_var.get())
            self.global_config['install_1c_extension'] = check_var.get() == "on"

        check_var = ctk.StringVar(value="on")
        self.global_config['install_1c_extension'] = True
        checkbox = ctk.CTkCheckBox(self.main_frame, text="Установка Расширения", command=checkbox_event,
                                             variable=check_var, onvalue="on", offvalue="off", checkbox_width=20,
                                   checkbox_height=20)
        checkbox.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-100)