import re
import ctypes
import subprocess


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
    pattern = re.compile(r'\[([^\]]+)\]\s+Connect=(.*)')
    matches = pattern.findall(file_content)
    return {key: value for key, value in matches}


def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
