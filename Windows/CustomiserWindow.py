from design_core import InstallerWindow
import customtkinter as ctk


class CustomiserWindow(InstallerWindow):
    header_text = 'Выбор компонентов'
    body_text = None

    @classmethod
    def can_draw(cls, global_config):
        return global_config.get("custom_mode", False)

    def draw(self):
        super().draw()

        def checkbox_event(variable_name, var):
            print(f"Пользователь нажал {variable_name}: {var.get()}")
            self.global_config[variable_name] = var.get() == "on"

        self.global_config['install_1c_extension'] = True
        check_vars = {
            'install_1c_extension': ctk.StringVar(value="on"),
            'install_apache': ctk.StringVar(value="on"),
            'publish_1c': ctk.StringVar(value="on"),
            'install_zf': ctk.StringVar(value="on"),
            'connect_database': ctk.StringVar(value="on"),
            'check_functionality': ctk.StringVar(value="on"),
        }

        checkboxes = {
            'install_1c_extension': "Установить расширение",
            'install_apache': "Установить Apache",
            'publish_1c': "Опубликовать 1С",
            'install_zf': "Установка ZF",
            'connect_database': "Подключение базы",
            'check_functionality': "Проверка работоспособности"
        }

        # Цветовая настройка флажков
        checkbox_style = {
            "fg_color": "#6EC756",  # Цвет флажка
            "hover_color": "#4EB932"  # Цвет при наведении мыши
        }

        # Размещение флажков
        y_offset = 0
        for key, text in checkboxes.items():
            checkbox = ctk.CTkCheckBox(
                self.main_frame, text=text, font=("Rubik Light", 12),
                command=lambda k=key, v=check_vars[key]: checkbox_event(k, v),
                variable=check_vars[key],
                onvalue="on", offvalue="off",
                checkbox_width=15, checkbox_height=15,
                text_color="black",  # Устанавливаем цвет текста флажка
                **checkbox_style
            )
            checkbox.place(relx=0.05, rely=0.32 + y_offset/100, anchor='nw')
            y_offset += 7
