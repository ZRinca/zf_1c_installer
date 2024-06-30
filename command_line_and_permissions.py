import os
import re
import subprocess
import ctypes
import time
from agent_mode import enter_commands_agent_mod


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def input_cmd(commands):
    if is_admin():
        subprocess.run(commands, check=True)
    else:
        full_command = ' && '.join(commands)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/K " + full_command, None, 1)


def run_as_admin(found_1c, found_base, login, password):
    try:
        input_cmd(["cd C:\\Apache24\\bin && httpd.exe -k install && net start Apache2.4"])

        # load_cfg_command = f'cd {found_1c} && 1cv8 DESIGNER /F"{link}" /LoadCfg "C:\\Apache24\\Api\\InterfaceAPI.cfe" -Extension "InterfaceAPI"'
        # input_cmd([load_cfg_command])

        publish_command = (
            f'cd {found_1c} && webinst -publish -apache24 -wsdir Base -dir "c:\\apache\\htdocs\\Base" '
            f'-connstr "File="{found_base[list(found_base.keys())[0]]}";" -confpath "C:\\Apache24\\conf\\httpd.conf" && net stop '
            f'Apache2.4 && net start Apache2.4')
        input_cmd([publish_command])

        agent_1c_start = (
            f'cd {found_1c} && cd ../../common && 1cestart.exe DESIGNER '
            f'/AgentMode /AgentBaseDir "C:\\Apache24\\Api" '
            f'/IBName "{list(found_base.keys())[0]}" '
            f'/AgentSSHHostKeyAuto /Visible'
        )

        input_cmd([agent_1c_start])
        time.sleep(15)
        enter_commands_agent_mod(login, password)

        return "Служба Apache успешно установлена и запущена."
    except subprocess.CalledProcessError as e:
        return f"Произошла ошибка при установке или запуске службы Apache: {e}"
    except Exception as e:
        return f"Произошла неожиданная ошибка: {e}"


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