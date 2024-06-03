import customtkinter as ctk
from tkinter import filedialog

# Данные для выпадающего списка
programs = {
    '1С:Предприятие 8 (учебная версия) (8.3.21.1393)': 'C:\\Program Files (x86)\\1cv8t\\8.3.21.1393\\',
    '1C:Enterprise 8 (training version) (8.3.22.1709)': 'C:\\Program Files (x86)\\1cv8t\\8.3.22.1709\\',
    '1C:Предприятие 8.2 (8.2.19.130)': 'C:\\Program Files (x86)\\1cv82\\8.2.19.130\\',
    '1С:Предприятие 8 (x86-64) (8.3.22.1750)': 'C:\\Program Files\\1cv8\\8.3.22.1750\\'
}

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: on_focus_in(event, placeholder))
    entry.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder))

def on_focus_in(event, placeholder):
    if event.widget.get() == placeholder:
        event.widget.delete(0, ctk.END)
        event.widget.configure(placeholder_text_color="black")

def on_focus_out(event, placeholder):
    if not event.widget.get():
        event.widget.insert(0, placeholder)
        event.widget.configure(placeholder_text_color="grey")

def open_first_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

    label1 = ctk.CTkLabel(main_frame, text="Салам", font=("Rubik Light", 12), anchor='w', text_color="#6EC756", justify='left', wraplength=main_frame.winfo_width()-48)
    label1.pack(padx=24, pady=(24, 0), fill='x')

    line = ctk.CTkFrame(main_frame, height=2, fg_color="#6EC756")
    line.pack(padx=24, pady=(24, 0), fill='x')

    label2 = ctk.CTkLabel(main_frame,
                          text="При нажатии на кнопку «Далее» вы принимаете условия лицензионного соглашения. Это \nозначает, "
                               "что вы соглашаетесь с правилами использования программного обеспечения или "
                               "\nдругого продукта, предоставляемого вам.",
                          font=("Rubik Light", 10), anchor='w', justify='left', wraplength=main_frame.winfo_width()-48)
    label2.pack(padx=24, pady=(24, 0), fill='x')

    button_next = ctk.CTkButton(main_frame, text="Далее", command=open_txt_page, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

def open_txt_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    label1 = ctk.CTkLabel(main_frame, text="Дайте мне txt", font=("Rubik Light", 12), anchor='w',
                          text_color="#6EC756", justify='left', wraplength=main_frame.winfo_width()-48)
    label1.pack(padx=24, pady=(24, 0), fill='x')

    line = ctk.CTkFrame(main_frame, height=2, fg_color="#6EC756")
    line.pack(padx=24, pady=(24, 0), fill='x')

    label2 = ctk.CTkLabel(main_frame,
                          text="Пожалуйста, вставьте сюда ваш уникальный ключ в формате TXT. Ключ можно найти в вашем \nличном кабинете. После того как вы вставите ключ, нажмите кнопку „Выбрать файл“ для \nзавершения процесса установки",
                          font=("Rubik Light", 10), anchor='w', justify='left', wraplength=main_frame.winfo_width()-48)
    label2.pack(padx=24, pady=(24, 0), fill='x')

    global file_path_label
    file_path_label = ctk.StringVar(value="")

    frame_file_selection = ctk.CTkFrame(main_frame, fg_color="transparent")
    frame_file_selection.pack(padx=24, pady=(24, 0), fill='x')  # 24 пикселя ниже label2

    entry_file_path = ctk.CTkEntry(frame_file_selection, textvariable=file_path_label, font=("Rubik Light", 12), border_color="grey", state="readonly")
    entry_file_path.pack(side="left", fill='x', expand=True, padx=(0, 10))

    button_select = ctk.CTkButton(frame_file_selection, text="Выбрать файл", command=select_txt_file, width=120, height=30, fg_color="#B3B7B1", hover_color="#8c9289")
    button_select.pack(side="right")

    button_back = ctk.CTkButton(main_frame, text="Назад", command=open_first_frame, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_back.place(relx=1.0, rely=1.0, anchor='se', x=-24 - 80 - 13, y=-24)

    button_next = ctk.CTkButton(main_frame, text="Далее", command=open_third_frame, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

def select_txt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_path_label.set(file_path)
        print(f"Выбранный файл: {file_path}")

def open_third_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

    label1 = ctk.CTkLabel(main_frame, text="Выберите 1C из списка", font=("Rubik Light", 12), anchor='w', text_color="#6EC756", justify='left', wraplength=main_frame.winfo_width()-48)
    label1.pack(padx=24, pady=(24, 0), fill='x')

    line = ctk.CTkFrame(main_frame, height=2, fg_color="#6EC756")
    line.pack(padx=24, pady=(24, 0), fill='x')

    label2 = ctk.CTkLabel(main_frame,
                          text="Программа нашла на вашем устройстве несколько установленных 1С. В списке ниже указаны все\nустановленные версии 1С.",
                          font=("Rubik Light", 10), anchor='w', justify='left', wraplength=main_frame.winfo_width()-48)
    label2.pack(padx=24, pady=(24, 0), fill='x')

    selected_program.set('')
    combobox = ctk.CTkComboBox(main_frame, variable=selected_program, values=list(programs.keys()), font=("Rubik Light", 12), border_color='#B3B7B1', button_color="#B3B7B1")
    combobox.pack(padx=24, pady=24, fill='x')

    button_back = ctk.CTkButton(main_frame, text="Назад", command=open_txt_page, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_back.place(relx=1.0, rely=1.0, anchor='se', x=-24 - 80 - 13, y=-24)
    button_next = ctk.CTkButton(main_frame, text="Далее", command=open_fourth_frame, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_next.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

def open_fourth_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

    label1 = ctk.CTkLabel(main_frame, text="Введите логин и пароль от вашей 1С.", font=("Rubik Light", 12), anchor='w',
                          text_color="#6EC756", justify='left', wraplength=main_frame.winfo_width()-48)
    label1.pack(padx=24, pady=(24, 0), fill='x')

    line = ctk.CTkFrame(main_frame, height=2, fg_color="#6EC756")
    line.pack(padx=24, pady=(24, 0), fill='x')

    label2 = ctk.CTkLabel(main_frame,
                          text="1С, которую вы выбрали, требует авторизации. Пожалуйста, введите логин и пароль.",
                          font=("Rubik Light", 10), anchor='w', justify='left', wraplength=main_frame.winfo_width()-48)
    label2.pack(padx=24, pady=(24, 0), fill='x')

    login_entry = ctk.CTkEntry(main_frame, font=("Arial", 14), placeholder_text="Логин", placeholder_text_color="grey")
    login_entry.pack(padx=24, pady=(24, 0), fill='x')

    password_entry = ctk.CTkEntry(main_frame, font=("Arial", 14), show='*', placeholder_text="Пароль", placeholder_text_color="grey")
    password_entry.pack(padx=24, pady=(13, 24), fill='x')

    button_back = ctk.CTkButton(main_frame, text="Назад", command=open_third_frame, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_back.place(relx=1.0, rely=1.0, anchor='se', x=-24 - 80 - 13, y=-24)
    button_submit = ctk.CTkButton(main_frame, text="Отправить", command=submit_form, width=80, height=30, fg_color="#6EC756", hover_color="#4EB932")
    button_submit.place(relx=1.0, rely=1.0, anchor='se', x=-24, y=-24)

def submit_form():
    show_selection()
    print("Форма отправлена")

def show_selection():
    selection = selected_program.get()
    print(f"Вы выбрали: {selection}")

def create_main_window():
    global main_frame, selected_program, file_path_label

    root = ctk.CTk()
    window_width = 522
    window_height = 329

    # Определение размеров экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисление координат верхнего левого угла для центрирования окна
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    root.title("Setup ZF")
    root.configure(bg="#F8F8F8")

    main_frame = ctk.CTkFrame(root, fg_color="#F8F8F8")
    main_frame.pack(fill='both', expand=True)

    selected_program = ctk.StringVar()

    open_first_frame()

    root.mainloop()

if __name__ == "__main__":
    create_main_window()