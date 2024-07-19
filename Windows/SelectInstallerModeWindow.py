from design_core import InstallerWindow
import customtkinter as ctk


class SelectInstallerModeWindow(InstallerWindow):
    header_text = 'Выбор режима установки!'
    body_text = 'Выберите режим установки'
    draw_next_button = False

    def open_customer_window(self):
        self.global_config['custom_mode'] = True
        self.open_next_window()

    def draw(self):
        super().draw()
        self.global_config['custom_mode'] = False

        button_full = ctk.CTkButton(self.main_frame, text="Полная установка", command=lambda: self.open_next_window(), width=80,
                                    height=30,
                                    fg_color="#6EC756", hover_color="#4EB932")
        button_full.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-64)

        button_custom = ctk.CTkButton(self.main_frame, text="Кастомная установка",
                                    command=lambda: self.open_customer_window(), width=80,
                                    height=30,
                                    fg_color="#6EC756", hover_color="#4EB932")
        button_custom.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-100)
