import customtkinter as ctk
import tkinter as tk
from itertools import cycle
from tkinter import filedialog
from search_1c import find_display_names

find_1c = find_display_names(r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall")  # Дополнительно получаем install_locations
find_1c_2 = find_display_names(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
programs = find_1c.copy()
programs.update(find_1c_2)


def select_txt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_path_label.set(file_path)


class LoadingIndicator(ctk.CTkCanvas):
    def __init__(self, master, size=100, speed=10, *args, **kwargs):
        super().__init__(master, width=size, height=size, bg="#F8F8F8", highlightthickness=0, *args, **kwargs)
        self.size = size
        self.speed = speed

        # Create the inner arc (part of the circle)
        self.inner_arc = self.create_arc((10, 10, size - 10, size - 10), start=0, extent=270, style=tk.ARC, outline="#EDF8F3", width=5)

        # Create the outer arc (part of the circle)
        self.outer_arc = self.create_arc((10, 10, size - 10, size - 10), start=0, extent=270, style=tk.ARC, outline="#88DE71", width=5)

        # List of angles for the arc start position with smaller steps
        self.angles = cycle(range(0, 360, 5))
        self.animate()

    def animate(self):
        # Update the start angle of the arcs
        angle = next(self.angles)
        self.itemconfig(self.inner_arc, start=angle)
        self.itemconfig(self.outer_arc, start=angle)  # Sync the outer arc with the inner arc
        self.after(self.speed, self.animate)


class InstallerWindow:

    def __init__(self, main_frame, title, description, open_window_back, open_window_next):
        self.title = title
        self.description = description
        self.main_frame = main_frame
        self.open_window_back = open_window_back
        self.open_window_next = open_window_next

    def draw(self):

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        label1 = ctk.CTkLabel(self.main_frame, text=self.title, font=("Rubik Light", 12), anchor='w',
                              text_color="#6EC756",
                              justify='left', wraplength=self.main_frame.winfo_width() - 48)
        label1.pack(padx=24, pady=(24, 0), fill='x')

        line = ctk.CTkFrame(self.main_frame, height=2, fg_color="#6EC756")
        line.pack(padx=24, pady=(24, 0), fill='x')

        label2 = ctk.CTkLabel(self.main_frame,
                              text=self.description,
                              font=("Rubik Light", 10), anchor='w', justify='left',
                              wraplength=self.main_frame.winfo_width() - 48)
        label2.pack(padx=24, pady=(24, 0), fill='x')

        if self.open_window_back:
            button_back = ctk.CTkButton(self.main_frame, text="Назад", command=self.open_window_back, width=80,
                                        height=30,
                                        fg_color="#6EC756", hover_color="#4EB932")
            button_back.place(relx=1.0, rely=1.0, anchor='se', x=-24 - 80 - 13, y=-24)

        button_next = ctk.CTkButton(self.main_frame, text="Далее", command=self.open_window_next, width=80, height=30,
                                    fg_color="#6EC756", hover_color="#4EB932")
        button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)


class FindFileWindow(InstallerWindow):

    def draw(self):
        super().draw()
        global file_path_label
        file_path_label = ctk.StringVar(value="")

        frame_file_selection = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame_file_selection.pack(padx=24, pady=(24, 0), fill='x')  # 24 пикселя ниже label2

        entry_file_path = ctk.CTkEntry(frame_file_selection, textvariable=file_path_label, font=("Rubik Light", 12),
                                       border_color="grey", state="readonly")
        entry_file_path.pack(side="left", fill='x', expand=True, padx=(0, 10))

        button_select = ctk.CTkButton(frame_file_selection, text="Выбрать файл", command=select_txt_file, width=120,
                                      height=30, fg_color="#B3B7B1", hover_color="#8c9289")
        button_select.pack(side="right")


class LoginPasswordWindow(InstallerWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.req_1c_login_password = False

    def draw(self):
        if self.req_1c_login_password:
            super().draw()
            login_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), placeholder_text="Логин",
                                       placeholder_text_color="grey")
            login_entry.pack(padx=24, pady=(24, 0), fill='x')

            password_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 14), show='*', placeholder_text="Пароль",
                                          placeholder_text_color="grey")
            password_entry.pack(padx=24, pady=(13, 24), fill='x')
        else:
            for widget in self.main_frame.winfo_children():
                widget.destroy()

            label1 = ctk.CTkLabel(self.main_frame, text=self.title, font=("Rubik Light", 12), anchor='w',
                                  text_color="#6EC756", justify='left', wraplength=self.main_frame.winfo_width() - 48)
            label1.pack(side="left", anchor="sw", padx=24, pady=24)

            loading = LoadingIndicator(self.main_frame, size=110, speed=10)
            loading.place(relx=0.5, rely=0.5, anchor="center")

# class Find1cList(InstallerWindow):
#
#     def draw(self):
#         super().draw()
#         combobox = ctk.CTkComboBox(self.main_frame, variable=selected_program, values=list(programs.keys()),
#                                    font=("Rubik Light", 12), border_color='#B3B7B1', button_color="#B3B7B1")
#         combobox.pack(padx=24, pady=24, fill='x')
