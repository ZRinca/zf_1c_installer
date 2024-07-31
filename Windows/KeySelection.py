from Windows.window_error import show_error_window
from design_core import InstallerWindow
from tkinter import filedialog
import customtkinter as ctk

from logic.command_line_and_permissions import sub_run

file_path = ""
file_path_label = None


def select_txt_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.dskey")])
    if file_path:
        file_path_label.set(file_path)
    else:
        file_path_label.set("")


class KSelection(InstallerWindow):
    header_text = "Выберите ваш персональный ключ"
    body_text = ("Пожалуйста, вставьте сюда ваш уникальный ключ в формате dskey.Ключ можно найти в вашем \nличном "
                 "кабинете. После того как вы вставите ключ, нажмите кнопку „Выбрать файл“ для завершения процесса "
                 "установки")
    draw_next_button = False
    draw_back_button = False

    @classmethod
    def can_draw(cls, global_config):
        keys_to_check = ['install_zf', 'check_functionality']
        all_false = not all(not global_config.get(key, True) for key in keys_to_check)
        return all_false

    def draw(self):
        super().draw()
        global file_path_label

        file_path_label = ctk.StringVar(value=file_path)

        frame_file_selection = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame_file_selection.pack(padx=24, pady=(24, 0), fill='x')

        entry_file_path = ctk.CTkEntry(frame_file_selection, textvariable=file_path_label, font=("Rubik Light", 12),
                                       border_color="grey", state="readonly")
        entry_file_path.pack(side="left", fill='x', expand=True, padx=(0, 10))

        button_select = ctk.CTkButton(frame_file_selection, text="Выбрать файл", command=select_txt_file, width=120,
                                      height=30, fg_color="#B3B7B1", hover_color="#8c9289")
        button_select.pack(side="right")

        button_next = ctk.CTkButton(self.main_frame, text="Далее", command=self.check_file_and_proceed, width=80,
                                    height=30, fg_color="#6EC756", hover_color="#4EB932")
        button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

    def check_file_and_proceed(self):
        global file_path
        if not file_path:
            show_error_window("Файл не выбран. \nПожалуйста, выберите файл.")
        else:
            self.global_config['link_key'] = file_path
            sub_run(r'SCHTASKS /Run /TN \ZeroFactor\ZFConnector')
            self.open_next_window()
