import json
import subprocess


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

    command = 'cd C:\\zf_connector && zf_connector.exe'
    subprocess.run(['cmd', '/c', 'start', 'cmd', '/k', command])