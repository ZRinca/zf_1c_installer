import shutil
import os


def copy_apache_and_exp(bit):
    target_dir = 'C:\\Apache24'
    source_dir = None
    if bit == 32:
        source_dir = r'../Apache/Apache_32/Apache24'
    if bit == 64:
        source_dir = r'../Apache/Apache_64/Apache24'
    copy_file(source_dir, target_dir)
    copy_file('../extension', "C:\\Apache24\\Api")
    return


def copy_file(source_dir, target_dir):
    if not os.path.exists(source_dir):
        return f"Исходная директория {source_dir} не существует."
    else:
        try:
            shutil.copytree(source_dir, target_dir)
            return f"Директория {source_dir} успешно скопирована в {target_dir}."
        except FileExistsError:
            return f"Целевая директория {target_dir} уже существует."
        except Exception as e:
            return f"Произошла ошибка: {e}"


def move_and_rename_deskey_file(src_file_path, new_filename, destination_folder):
    try:
        if not os.path.isfile(src_file_path):
            print(f"Файл '{src_file_path}' не найден.")
            return

        if not os.path.isdir(destination_folder):
            print(f"Папка '{destination_folder}' не существует.")
            return

        new_file_path = os.path.join(destination_folder, new_filename)

        shutil.move(src_file_path, new_file_path)
        print(f"Файл успешно перемещен и переименован в '{new_file_path}'.")
    except Exception as e:
        print(f"Ошибка при перемещении файла: {e}")
