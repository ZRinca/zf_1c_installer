from settings import header_text_size, body_text_size, font_text, installer_version
from threading import Thread
import tkinter.messagebox as messagebox
import customtkinter as ctk
import webbrowser
import ctypes
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
    site_link = None
    draw_next_button = True
    draw_back_button = True
    installer_version = False
    technical_function = None

    def __init__(self, main_frame, global_config, prev_window_getter, next_window_getter):
        self.global_config = global_config
        self.main_frame = main_frame
        self.prev_window_getter = prev_window_getter
        self.next_window_getter = next_window_getter

    def run_tech_task(self, wait=True):
        if self.technical_function is None:
            return None
        result = [None]

        def _thread_wrapper(gc, res_arr):
            res_arr[0] = self.technical_function(gc)

        cur_thread = Thread(target=_thread_wrapper, args=(self.global_config, result,))
        cur_thread.start()
        if wait:
            cur_thread.join()
        return result[0]

    @classmethod
    def can_draw(cls, global_config):
        return True

    def open_next_window(self):
        open_window(self.main_frame, self.global_config, self.next_window_getter(self))

    def open_prev_window(self):
        open_window(self.main_frame, self.global_config, self.prev_window_getter(self))

    def draw(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if self.header_text is not None:
            label1 = ctk.CTkLabel(self.main_frame, text=self.header_text, font=(font_text, header_text_size),
                                  anchor='w',
                                  text_color="#6EC756",
                                  justify='left', wraplength=self.main_frame.winfo_width() - 48)
            label1.pack(padx=24, pady=(24, 0), fill='x')

            line = ctk.CTkFrame(self.main_frame, height=2, fg_color="#6EC756")
            line.pack(padx=24, pady=(24, 0), fill='x')

        if self.body_text is not None:
            label2 = ctk.CTkLabel(self.main_frame,
                                  text=self.body_text,
                                  font=(font_text, body_text_size), anchor='w', justify='left',
                                  wraplength=self.main_frame.winfo_width() - 48)
            label2.pack(padx=24, pady=(24, 0), fill='x')

        if self.site_link is not None:
            site_frame = ctk.CTkFrame(self.main_frame,
                                      fg_color="#F8F8F8")
            site_frame.pack(padx=24, pady=6, fill='x', anchor='w')

            site_label = ctk.CTkLabel(site_frame, text="Наш сайт:", font=(font_text, body_text_size), text_color="black")
            site_label.pack(side='left')

            link_label = ctk.CTkLabel(site_frame, text=self.site_link, font=(font_text, body_text_size, "underline"),
                                      text_color="blue", cursor="hand2")
            link_label.pack(side='left')
            link_label.bind("<Button-1>", lambda event: open_web(self.site_link))

        prev_win = self.prev_window_getter(self) if self.draw_back_button else None

        if self.installer_version:
            label_version = ctk.CTkLabel(self.main_frame, text=installer_version, font=("Arial", 12),
                                         text_color="grey", anchor='sw', justify='left')
            label_version.pack(side='bottom', anchor='sw', padx=24, pady=24)

        if prev_win is not None:
            button_back = ctk.CTkButton(self.main_frame, text="Назад", command=lambda: self.open_prev_window(),
                                        width=80,
                                        height=30,
                                        fg_color="#6EC756", hover_color="#4EB932")
            button_back.place(relx=1.0, rely=1.0, anchor='se', x=-24 - 80 - 13, y=-24)

        next_win = self.next_window_getter(self) if self.draw_next_button else None

        if next_win is not None:
            button_next = ctk.CTkButton(self.main_frame, text="Далее", command=lambda: self.open_next_window(),
                                        width=80,
                                        height=30,
                                        fg_color="#6EC756", hover_color="#4EB932")
            button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)


def get_prev_window(cur_win):
    back_index = cur_win.index - 1
    while back_index > -1:
        if ALL_WINDOWS[back_index].can_draw(cur_win.global_config):
            return ALL_WINDOWS[back_index]
        back_index -= 1
    return ALL_WINDOWS[cur_win.index - 1]


def get_next_window(cur_win):
    next_index = cur_win.index + 1
    while next_index < len(ALL_WINDOWS):
        if ALL_WINDOWS[next_index].can_draw(cur_win.global_config):
            return ALL_WINDOWS[next_index]
        next_index += 1
    return None


def open_window(main_frame, global_config, new_win):
    for widget in main_frame.winfo_children():
        widget.destroy()

    win_instance = new_win(main_frame, global_config, get_prev_window, get_next_window)
    win_instance.draw()


def check_for_admin(root):
    if not ctypes.windll.shell32.IsUserAnAdmin():
        messagebox.showwarning("Предупреждение", "Запустите установщик от имени администратора!")
        root.destroy()


def open_web(link):
    webbrowser.open_new(link)


def run_design(global_config):
    root = ctk.CTk()
    exe_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(exe_path, 'ico', 'ZF_green.ico')

    root.iconbitmap(icon_path)
    check_for_admin(root)

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
    root.resizable(False, False)

    main_frame = ctk.CTkFrame(root, fg_color="#F8F8F8")
    main_frame.pack(fill='both', expand=True)

    open_window(main_frame, global_config, ALL_WINDOWS[0])

    root.mainloop()
