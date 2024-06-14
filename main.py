from window_creator import *
from exe_bit_extractor import exe_bit
from installing_apache import inst_apache

selected_value = None


def open_first_frame():
    hello_window = InstallerWindow(main_frame, "Приветствую",
                                   "При нажатии на кнопку «Далее» вы принимаете условия лицензионного соглашения."
                                   "Это \нозначает, что вы соглашаетесь с правилами использования программного "
                                   "обеспечения или"
                                   "\ндругого продукта, предоставляемого вам.", None, open_txt_page)
    hello_window.draw()


def open_txt_page():
    txt_key_window = FindFileWindow(main_frame, "Дайте мне txt", "Пожалуйста, вставьте сюда ваш уникальный ключ в "
                                                                 "формате TXT."
                                                                 "Ключ можно найти в вашем \нличном кабинете. После того как вы вставите ключ, "
                                                                 "нажмите кнопку „Выбрать файл“ для "
                                                                 "\нзавершения процесса установки", open_first_frame,
                                    open_third_frame)

    txt_key_window.draw()


def open_third_frame():
    find_1c_window = InstallerWindow(main_frame, "Выберите 1C из списка", "Программа нашла на вашем устройстве "
                                                                          "несколько установленных 1С."
                                                                          "В списке ниже указаны все\nустановленные "
                                                                          "версии 1С.", open_txt_page, open_fourth_frame)
    find_1c_window.draw()
    selected_program.set('')
    combobox = ctk.CTkComboBox(main_frame, variable=selected_program, values=list(programs.keys()),
                               font=("Rubik Light", 12), border_color='#B3B7B1', button_color="#B3B7B1")
    combobox.pack(padx=24, pady=24, fill='x')


def open_fourth_frame():
    global selected_value
    selected_value = selected_program.get()
    if not selected_value:
        show_error_window("Не выбрана версия 1С.")
        return

    registration_window = LoginPasswordWindow(main_frame, "Введите логин и пароль от вашей 1С.",
                                              "1С, которую вы выбрали, требует"
                                              "авторизации. Пожалуйста, "
                                              "введите логин и пароль.",
                                              open_third_frame, None)
    registration_window.draw()

    loading = LoadingIndicator(main_frame, label_text="Загрузка данных...")
    loading.place(relx=0.5, rely=0.5, anchor="center")
    destroy_window(main_frame)

    print(programs[selected_value])

    loading = LoadingIndicator(main_frame, label_text="Узнаём какая битность у 1с")
    loading.place(relx=0.5, rely=0.5, anchor="center")
    destroy_window(main_frame)

    bit = exe_bit(f'{programs[selected_value]}\\bin\\1cv8.exe')
    # inst_apache(bit)
    print(bit)

    loading = LoadingIndicator(main_frame, label_text="Устанавливаем Apache")
    loading.place(relx=0.5, rely=0.5, anchor="center")

    inst_apache(bit, f'{programs[selected_value]}\\bin', 'C://bases//buh')

    destroy_window(main_frame)
    loading = LoadingIndicator(main_frame, label_text="Apache установлен")
    loading.place(relx=0.5, rely=0.5, anchor="center")

    destroy_window(main_frame)
    Final = FinalWindow(main_frame, "Установка завершена", "Установка завершена, и Zero Factor установлен. Спасибо, что выбрали нас!", None, None, root)
    Final.draw()
    # root.destroy()


def create_main_window():
    global main_frame, selected_program, file_path_label, root

    root = ctk.CTk()
    window_width = 522
    window_height = 329

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
