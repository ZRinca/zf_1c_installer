from logic.command_line_and_permissions import find_1c_base_list
from design_core import InstallerWindow
import customtkinter as ctk


class DataBaseSelection(InstallerWindow):
    header_text = "Выберите базу из списка"
    body_text = "Программа нашла на вашем устройстве несколько установленных баз.В списке ниже указаны все\nустановленныебазы 1С."

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_1c_extension', 'publish_1c', 'connect_database', 'check_functionality']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        databases = find_1c_base_list()
        self.global_config['base'] = databases

        self.database_combobox = ctk.CTkComboBox(self.main_frame, values=list(databases.keys()),
                                                 font=("Rubik Light", 12),
                                                 state="readonly", border_color='#B3B7B1', button_color="#B3B7B1")
        self.database_combobox.pack(padx=24, pady=24, fill='x')

        button_next = ctk.CTkButton(self.main_frame, text="Далее", command=self.on_next_button_click,
                                    width=80, height=30,
                                    fg_color="#6EC756", hover_color="#4EB932")
        button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

    def send_to_chat(self):
        selected_value = self.database_combobox.get()
        self.global_config['base_the_One_C'] = selected_value
        print(self.global_config)

    def on_next_button_click(self):
        self.send_to_chat()
        self.open_next_window()
