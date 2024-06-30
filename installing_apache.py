from command_line_and_permissions import run_as_admin
import shutil
import os


def inst_apache_and_exp(bit, found_1c, found_base, login, password):
    target_dir = 'C:\\Apache24'
    print(target_dir)
    source_dir = None
    if bit == 32:
        source_dir = r'Apache/Apache_32/Apache24'
    if bit == 64:
        source_dir = r'Apache/Apache_64/Apache24'
    copy_file(source_dir, target_dir)
    copy_file('expansion', "C:\\Apache24\\Api")
    run_as_admin(found_1c, found_base, login, password)
    return "Apache установлен"


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
