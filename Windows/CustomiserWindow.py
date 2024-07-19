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
            print("checkbox toggled, current value:", check_var.get())

        check_var = ctk.StringVar(value="on")
        checkbox = ctk.CTkCheckBox(self.main_frame, text="CTkCheckBox", command=checkbox_event,
                                             variable=check_var, onvalue="on", offvalue="off")
