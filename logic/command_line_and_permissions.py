import os
import re
import subprocess
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def input_cmd(commands):
    print('Start run commands', commands)
    try:
        if is_admin():
            result = subprocess.run(commands, check=True, shell=True, text=True, capture_output=True)
            print(result.stdout)
        else:
            full_command = ' && '.join(commands)
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/K " + full_command, None, 1)
        print('End run commands', commands)
    except Exception as e:
        print("Run commands exception", e)


def sub_run(commands):
    print(commands)
    p = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       encoding='CP866')
    if p.stderr == '':
        return p.stdout
    if p.stdout == '':
        return p.stderr
    else:
        return 'output is empty !'


def extract_bases(file_content):
    """
    Extracts all database entries (keys and paths) from the given content.
    Returns a dictionary with keys as base names and values as paths.
    """
    pattern = re.compile(r'\[([^\]]+)\]\s+Connect=File="(.+?)";')
    matches = pattern.findall(file_content)
    return {key: value for key, value in matches}


def read_file_content(file_path):
    """Reads and returns the content of the specified file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_1c_base_list():
    appdata_path = os.getenv('APPDATA')

    file_path = os.path.join(appdata_path, '1C', '1CEStart', 'ibases.v8i')

    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return {}

    content = read_file_content(file_path)
    bases = extract_bases(content)

    if bases:
        return bases
    else:
        print("No bases found.")
        return {}


bases = find_1c_base_list()
if bases:
    print("Найденные базы 1С:")
    for base, path in bases.items():
        print(f"{base}: {path}")
else:
    print("Базы 1С не найдены.")
