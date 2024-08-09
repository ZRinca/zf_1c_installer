from Windows.window_error import show_error_window
from logic.logic_function import find_full_1c
from design_core import InstallerWindow
import customtkinter as ctk


class OneCSelection(InstallerWindow):
    header_text = "Выберите 1C из списка", "Программа нашла на вашем устройстве "
    body_text = ("Программа нашла на вашем устройстве несколько установленных 1С.В списке ниже указаны все "
                 "установленные версии 1С.")
    draw_next_button = False

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_1c_extension', 'publish_1c', 'connect_database', 'check_functionality',
                         'install_apache']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()

        found_all_One_C = find_full_1c()

        self.global_config['One_C'] = found_all_One_C

        self.database_combobox = ctk.CTkComboBox(self.main_frame, values=list(found_all_One_C.keys()),
                                                 font=("Rubik Light", 12),
                                                 state="readonly", border_color='#B3B7B1', button_color="#B3B7B1")
        self.database_combobox.pack(padx=24, pady=24, fill='x')

        button_next = ctk.CTkButton(self.main_frame, text="Далее", command=self.on_next_button_click,
                                    width=80, height=30,
                                    fg_color="#6EC756", hover_color="#4EB932")
        button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

        if found_all_One_C:
            first_key = list(found_all_One_C.keys())[0]
            self.database_combobox.set(first_key)
            print('heyy')

    def write_value(self):
        selected_value = self.database_combobox.get()
        self.global_config['One_C_the_user'] = selected_value

    def on_next_button_click(self):
        if self.database_combobox.get() == '':
            show_error_window("Выберите базу!")
        else:
            self.write_value()
            self.open_next_window()
