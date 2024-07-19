from design_core import InstallerWindow
import customtkinter as ctk


def any_function(global_config):
    global_config['test2'] = 'shpek'


class HelloWindow(InstallerWindow):
    header_text = 'Приветствую!'
    body_text = 'Это приветственное окно!'

    def draw(self):
        # print(self.global_config)
        # any_function(self.global_config)
        # print(self.global_config)

        super().draw()

        frame_file_selection = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame_file_selection.pack(padx=24, pady=(24, 0), fill='x')  # 24 пикселя ниже label2

        entry_file_path = ctk.CTkEntry(frame_file_selection, font=("Rubik Light", 12),
                                       border_color="grey", state="readonly")
        entry_file_path.pack(side="left", fill='x', expand=True, padx=(0, 10))


class HelloNextWindow(InstallerWindow):
    header_text = 'Приветствую 2!'
    body_text = 'Это приветственное окно 2!'

    def draw(self):
        # print(self.global_config)
        # any_function(self.global_config)
        # print(self.global_config)

        super().draw()

        frame_file_selection = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame_file_selection.pack(padx=24, pady=(24, 0), fill='x')  # 24 пикселя ниже label2

        entry_file_path = ctk.CTkEntry(frame_file_selection, font=("Rubik Light", 12),
                                       border_color="grey", state="readonly")
        entry_file_path.pack(side="left", fill='x', expand=True, padx=(0, 10))


class HelloLastWindow(InstallerWindow):
    header_text = 'Приветствую 3!'
    body_text = 'Это приветственное окно 3!'

    def draw(self):
        # print(self.global_config)
        # any_function(self.global_config)
        # print(self.global_config)

        super().draw()

        frame_file_selection = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame_file_selection.pack(padx=24, pady=(24, 0), fill='x')  # 24 пикселя ниже label2

        entry_file_path = ctk.CTkEntry(frame_file_selection, font=("Rubik Light", 12),
                                       border_color="grey", state="readonly")
        entry_file_path.pack(side="left", fill='x', expand=True, padx=(0, 10))
