import threading
from window_creator import *
from exe_bit_extractor import exe_bit
from find_status_code import checking_code_status
from installing_apache import inst_apache_and_exp
from command_line_and_permissions import find_1c_base_list
import os

selected_value = None
selected_db = None
login = None
password = None


def open_first_frame():
    hello_window = InstallerWindow(main_frame, "Приветствую",
                                   "При нажатии на кнопку «Далее» вы принимаете условия лицензионного соглашения."
                                   "Это \n значает, что вы соглашаетесь с правилами использования программного "
                                   "обеспечения или"
                                   "\nдругого продукта, предоставляемого вам.", None, open_txt_page)
    hello_window.draw()


def open_txt_page():
    txt_key_window = FindFileWindow(main_frame, "Дайте мне txt", "Пожалуйста, вставьте сюда ваш уникальный ключ в "
                                                                 "формате TXT."
                                                                 "Ключ можно найти в вашем \nличном кабинете. После того как вы вставите ключ, "
                                                                 "нажмите кнопку „Выбрать файл“ для "
                                                                 "\nзавершения процесса установки", open_first_frame,
                                    open_third_frame)
    txt_key_window.draw()


def open_third_frame():
    global selected_value
    find_1c_window = InstallerWindow(main_frame, "Выберите 1C из списка", "Программа нашла на вашем устройстве "
                                                                          "несколько установленных 1С."
                                                                          "В списке ниже указаны все\nустановленные "
                                                                          "версии 1С.", open_txt_page,
                                     Open_list_of_databases)
    find_1c_window.draw()
    combobox = ctk.CTkComboBox(main_frame, variable=selected_program, values=list(programs.keys()),
                               font=("Rubik Light", 12), state="readonly", border_color='#B3B7B1',
                               button_color="#B3B7B1")
    combobox.pack(padx=24, pady=24, fill='x')

    if not list(programs.keys()):
        show_error_window('Не найдено ни одной 1с')

    if selected_value:
        selected_program.set(selected_value)


def Open_list_of_databases():
    global selected_db
    global databases
    global selected_value
    selected_value = selected_program.get()
    if not selected_value:
        show_error_window("Не выбрана версия 1С.")
        return

    databases = find_1c_base_list()
    find_1c_window = InstallerWindow(main_frame, "Выберите базу из списка", "Программа нашла на вашем устройстве "
                                                                            "несколько установленных баз."
                                                                            "В списке ниже указаны все\nустановленные "
                                                                            "базы 1С.", open_third_frame,
                                     login_and_password)
    find_1c_window.draw()
    database_combobox = ctk.CTkComboBox(main_frame, variable=selected_bd_programm, values=list(databases.keys()),
                                        font=("Rubik Light", 12),
                                        state="readonly", border_color='#B3B7B1', button_color="#B3B7B1")
    database_combobox.pack(padx=24, pady=24, fill='x')
    if selected_db:
        selected_bd_programm.set(selected_db)


def execute_in_thread(target, *args):
    thread = threading.Thread(target=target, args=args)
    thread.start()


def login_and_password():
    global login_entry, password_entry
    registration_window = LoginPasswordWindow(main_frame, "Введите логин и пароль от вашей 1С.",
                                              "1С, которую вы выбрали, требует"
                                              "авторизации. \nПожалуйста, "
                                              "введите логин и пароль.",
                                              open_third_frame, open_fourth_frame)
    registration_window.draw()

    login_entry = ctk.CTkEntry(main_frame, font=("Arial", 14), placeholder_text="Логин",
                               placeholder_text_color="grey")
    login_entry.pack(padx=24, pady=(24, 0), fill='x')

    password_entry = ctk.CTkEntry(main_frame, font=("Arial", 14), show='*', placeholder_text="Пароль",
                                  placeholder_text_color="grey")
    password_entry.pack(padx=24, pady=(13, 24), fill='x')


def open_fourth_frame():
    global login, password, selected_value

    login = login_entry.get()
    password = password_entry.get()

    selected_value = selected_program.get()
    if not selected_value:
        show_error_window("Не выбрана версия 1С.")
        return

    loading = LoadingIndicator(main_frame, label_text="Загрузка данных...")
    loading.place(relx=0.5, rely=0.5, anchor="center")
    destroy_window(main_frame)

    execute_in_thread(process_installation)


def process_installation():

    loading = LoadingIndicator(main_frame, label_text="Узнаём какая битность у 1с")
    loading.place(relx=0.5, rely=0.5, anchor="center")
    destroy_window(main_frame)
    if checking_code_status() == 200:
        print("Соединение есть")
    bit = exe_bit(f'{programs[selected_value]}\\bin\\1cv8.exe')

    loading = LoadingIndicator(main_frame, label_text="Устанавливаем утилиты")
    loading.place(relx=0.5, rely=0.5, anchor="center")
    inst_apache_and_exp(bit, f'{programs[selected_value]}\\bin', databases, login, password)

    destroy_window(main_frame)
    loading = LoadingIndicator(main_frame, label_text="утилиты установлены")
    loading.place(relx=0.5, rely=0.5, anchor="center")

    destroy_window(main_frame)
    Final = FinalWindow(main_frame, "Установка завершена",
                        "Установка завершена, и Zero Factor установлен. Спасибо, что выбрали нас!", None, None, root)
    Final.draw()


def create_main_window():
    global main_frame, selected_program, selected_bd_programm, file_path_label, root

    root = ctk.CTk()

    exe_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(exe_path, 'ico', 'ZF_green.ico')

    root.iconbitmap(icon_path)

    window_width = 522
    window_height = 329

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    root.title("Setup ZF-Connector")
    root.configure(bg="#F8F8F8")

    main_frame = ctk.CTkFrame(root, fg_color="#F8F8F8")
    main_frame.pack(fill='both', expand=True)

    selected_program = ctk.StringVar()
    selected_bd_programm = ctk.StringVar()

    open_first_frame()

    root.mainloop()


if __name__ == "__main__":
    create_main_window()