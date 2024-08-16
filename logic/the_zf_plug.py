import shutil
import os


def replace_text_in_xml(file_path, target_text, replacement_text):
    try:
        with open(file_path, 'r', encoding='utf-16') as file:
            content = file.read()

        new_content = content.replace(target_text, replacement_text)

        with open(file_path, 'w', encoding='utf-16') as file:
            file.write(new_content)

        print(f"Заменён текст '{target_text}' на '{replacement_text}' в файле {file_path}.")

    except Exception as e:
        print(f'Произошла ошибка: {e}')


def create_file_folder_zf():
    base_path = r'C:\zf_connector\base_'
    source_dir = r'output'

    i = 1

    while True:
        path = f'{base_path}{i}'
        if not os.path.exists(path):
            os.mkdir(path)
            print(f'Создана папка: {path}')

            for item in os.listdir(source_dir):
                s = os.path.join(source_dir, item)
                d = os.path.join(path, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            break
        i += 1
    return path, i

