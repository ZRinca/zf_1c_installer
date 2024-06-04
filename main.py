import customtkinter as ctk
from window_creator import InstallerWindow, FindFileWindow, LoginPassword

# Данные для выпадающего списка
programs = {
    '1С:Предприятие 8 (учебная версия) (8.3.21.1393)': 'C:\\Program Files (x86)\\1cv8t\\8.3.21.1393\\',
    '1C:Enterprise 8 (training version) (8.3.22.1709)': 'C:\\Program Files (x86)\\1cv8t\\8.3.22.1709\\',
    '1C:Предприятие 8.2 (8.2.19.130)': 'C:\\Program Files (x86)\\1cv82\\8.2.19.130\\',
    '1С:Предприятие 8 (x86-64) (8.3.22.1750)': 'C:\\Program Files\\1cv8\\8.3.22.1750\\'
}


def open_first_frame():

    hello_window = InstallerWindow(main_frame, "Приветствую",
                                   "При нажатии на кнопку «Далее» вы принимаете условия лицензионного соглашения."
                                   "Это \nозначает, ""что вы соглашаетесь с правилами использования программного обеспечения или "
                                   "\nдругого продукта, предоставляемого вам.", None, open_txt_page)
    hello_window.draw()


def open_txt_page():


    txt_key_window = FindFileWindow(main_frame, "Дайте мне txt", "Пожалуйста, вставьте сюда ваш уникальный ключ в "
                                                                 "формате TXT."
                                                                 "Ключ можно найти в вашем \nличном кабинете. После того как вы вставите ключ, "
                                                                 "нажмите кнопку „Выбрать файл“ для "
                                                                 "\nзавершения процесса установки", open_first_frame, open_third_frame)

    txt_key_window.draw()


def open_third_frame():

    find_1c_window = InstallerWindow(main_frame, "Выберите 1C из списка", "Программа нашла на вашем устройстве "
                                                                          "несколько установленных 1С."
                                                                          "В списке ниже указаны все\nустановленные "
                                                                          "версии 1С.", open_txt_page,open_fourth_frame)
    find_1c_window.draw()

    selected_program.set('')
    combobox = ctk.CTkComboBox(main_frame, variable=selected_program, values=list(programs.keys()),
                               font=("Rubik Light", 12), border_color='#B3B7B1', button_color="#B3B7B1")
    combobox.pack(padx=24, pady=24, fill='x')


def open_fourth_frame():
    registration_window = LoginPassword(main_frame, "Введите логин и пароль от вашей 1С.",
                                        "1С, которую вы выбрали, требует"
                                        "авторизации. Пожалуйста, "
                                        "введите логин и пароль.",
                                        open_third_frame, show_selection)
    registration_window.draw()


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
