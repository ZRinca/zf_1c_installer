import json
import os
import shutil
import subprocess
from settings import the_path_to_zf


def json_settings():

    json_file = "../zf_1c_connect_client/settings.json"

    new_data_server_url = "http://localhost/Base/"

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл не найден: {json_file}")
        exit()

    data['data_server_url'] = new_data_server_url

    try:
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Значение ключа 'data_server_url' успешно изменено на '{new_data_server_url}' в файле {json_file}.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")


def zf_plug():
    command = f'cd {the_path_to_zf} && zf_connector.exe'
    subprocess.run(['cmd', '/c', 'start', 'cmd', '/k', command])


def create_file_folder_zf():
    base_path = r"C:\zf_connector\base_"  # Используем сырую строку
    source_dir = 'output'

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
