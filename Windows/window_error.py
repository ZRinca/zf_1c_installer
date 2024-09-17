from settings import ico_core
import customtkinter as ctk
import tkinter as tk
import os

error_window = None


def notifications_window(message, error=True, user_function=None):
    global error_window

    if error_window is not None and error_window.winfo_exists():
        return

    exe_path = os.path.dirname(os.path.abspath(__file__))

    error_window = tk.Toplevel()
    error_window.title("Уведомление")
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

    button_frame = tk.Frame(error_window, bg="#F8F8F8")
    button_frame.pack(pady=(24, 24))

    close_button = ctk.CTkButton(button_frame, text="Закрыть", command=close_error_window,
                                 fg_color="#6EC756", hover_color="#4EB932", width=80, height=30)
    close_button.grid(row=0, column=0, padx=10)  # Располагаем в первой колонке

    if not error:
        def install_and_close():
            if user_function:
                user_function()
            close_error_window()

        install_button = ctk.CTkButton(button_frame, text="Установить", command=install_and_close,
                                       fg_color="#6EC756", hover_color="#4EB932", width=80, height=30)
        install_button.grid(row=0, column=1, padx=10)


def close_error_window():
    global error_window
    if error_window is not None:
        error_window.destroy()
        error_window = None
