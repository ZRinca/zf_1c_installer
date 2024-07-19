import customtkinter as ctk
import os


ALL_WINDOWS = []


class InstallerWindowBase(type):
    def __new__(mcs, name, *args, **kwargs):
        ans = super().__new__(mcs, name, *args, **kwargs)
        if name != 'InstallerWindow':
            idx = len(ALL_WINDOWS)
            ALL_WINDOWS.append(ans)
            ans.index = idx
        return ans


class InstallerWindow(metaclass=InstallerWindowBase):
    header_text = None
    body_text = None

    def __init__(self, main_frame, global_config, prev_window_getter, next_window_getter):
        self.global_config = global_config
        self.main_frame = main_frame
        self.prev_window_getter = prev_window_getter
        self.next_window_getter = next_window_getter

    def open_window(self, new_win):
        open_window(self.main_frame, self.global_config, new_win)

    def draw(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if self.header_text is not None:
            label1 = ctk.CTkLabel(self.main_frame, text=self.header_text, font=("Rubik Light", 12), anchor='w',
                                  text_color="#6EC756",
                                  justify='left', wraplength=self.main_frame.winfo_width() - 48)
            label1.pack(padx=24, pady=(24, 0), fill='x')

            line = ctk.CTkFrame(self.main_frame, height=2, fg_color="#6EC756")
            line.pack(padx=24, pady=(24, 0), fill='x')

        if self.body_text is not None:
            label2 = ctk.CTkLabel(self.main_frame,
                                  text=self.body_text,
                                  font=("Rubik Light", 10), anchor='w', justify='left',
                                  wraplength=self.main_frame.winfo_width() - 48)
            label2.pack(padx=24, pady=(24, 0), fill='x')

        prev_win = self.prev_window_getter(self)

        if prev_win is not None:
            button_back = ctk.CTkButton(self.main_frame, text="Назад", command=lambda: self.open_window(prev_win), width=80,
                                        height=30,
                                        fg_color="#6EC756", hover_color="#4EB932")
            button_back.place(relx=1.0, rely=1.0, anchor='se', x=-24 - 80 - 13, y=-24)

        next_win = self.next_window_getter(self)

        if next_win is not None:
            button_next = ctk.CTkButton(self.main_frame, text="Далее", command=lambda: self.open_window(next_win), width=80,
                                        height=30,
                                        fg_color="#6EC756", hover_color="#4EB932")
            button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)


def get_prev_window(cur_win):
    if cur_win.index < 1:
        return None

    return ALL_WINDOWS[cur_win.index - 1]


def get_next_window(cur_win):
    if cur_win.index >= len(ALL_WINDOWS) - 1:
        return None

    return ALL_WINDOWS[cur_win.index + 1]


def open_window(main_frame, global_config, new_win):
    for widget in main_frame.winfo_children():
        widget.destroy()

    first_win = new_win(main_frame, global_config, get_prev_window, get_next_window)
    first_win.draw()


def run_design(global_config):
    root = ctk.CTk()

    exe_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(exe_path, 'ico', 'ZF_green.ico')

    root.iconbitmap(icon_path)

    window_width = 522
    window_height = 329

    # root.attributes("-topmost", True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    root.title("Setup ZF-Connector")
    root.configure(bg="#F8F8F8")

    main_frame = ctk.CTkFrame(root, fg_color="#F8F8F8")
    main_frame.pack(fill='both', expand=True)

    # selected_program = ctk.StringVar()
    # selected_bd_programm = ctk.StringVar()

    open_window(main_frame, global_config, ALL_WINDOWS[0])

    root.mainloop()
