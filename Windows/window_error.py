import customtkinter as ctk
import tkinter as tk
import os

from settings import ico_core

file_path = None
error_window = None
login = ''
password = ''


def show_error_window(message):
    global error_window

    if error_window is not None and error_window.winfo_exists():
        return

    exe_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(exe_path, 'ico', 'ZF_green.ico')

    error_window = tk.Toplevel()
    error_window.title("Ошибка")
    error_window.configure(bg="#F8F8F8")
    error_window.iconbitmap(ico_core)

    window_width = 270
    window_height = 160
    screen_width = error_window.winfo_screenwidth()
    screen_height = error_window.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    error_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    label = ctk.CTkLabel(error_window, text=message, font=("Arial", 12))
    label.pack(pady=(24, 0))

    button = ctk.CTkButton(error_window, text="Закрыть", command=close_error_window, fg_color="#6EC756",
                           hover_color="#4EB932", width=80, height=30)
    button.pack(pady=(24, 24))


def close_error_window():
    global error_window
    if error_window is not None:
        error_window.destroy()
        error_window = None
