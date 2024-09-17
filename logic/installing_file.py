from Windows.window_error import notifications_window
import shutil
import os


def copy_file(source_dir, target_dir):
    if not os.path.exists(source_dir):
        return f'Исходная папка {source_dir} не существует.'

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            target_item = os.path.join(target_dir, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, target_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, target_item)

        return f'Файлы из {source_dir} успешно скопированы в {target_dir}.'
    except Exception as e:
        notifications_window(f'Произошла ошибка: {e}')
        return


def move_and_rename_deskey_file(src_file_path, new_filename, destination_folder):
    try:
        if not os.path.isfile(src_file_path):
            print(f"Файл '{src_file_path}' не найден.")
            return

        if not os.path.isdir(destination_folder):
            print(f"Папка '{destination_folder}' не существует.")
            return

        new_file_path = os.path.join(destination_folder, new_filename)

        shutil.copy(src_file_path, new_file_path)
        print(f"Файл успешно перемещен и переименован в '{new_file_path}'.")
    except Exception as e:
        print(f'Ошибка при перемещении файла: {e}')
