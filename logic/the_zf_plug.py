import json
import subprocess
from settings import the_path_to_zf
from logic.installing_file import copy_file
from logic.command_line_and_permissions import sub_run


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


def install_zf(caller_window, global_config):
    copy_file('zf_1c_connect_client', the_path_to_zf)
    sub_run(r'SCHTASKS /Create /TN \ZeroFactor\ZFConnector /XML C:\Apache24\Api\ZFConnector_settings.xml')
    caller_window.open_next_window()
