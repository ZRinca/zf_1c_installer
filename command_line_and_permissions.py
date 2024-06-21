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
    if is_admin():
        subprocess.run(commands, check=True)
    else:
        full_command = ' && '.join(commands)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/K " + full_command, None, 1)


def run_as_admin(found_1c, found_base):
    try:
        input_cmd(["cd C:\\Apache24\\bin && httpd.exe -k install && net start Apache2.4"])

        for link in found_base:
            load_cfg_command = f'cd {found_1c} && 1cv8 DESIGNER /F"{link}" /LoadCfg "C:\\Apache24\\Api\\InterfaceAPI.cfe" -Extension "InterfaceAPI"'
            input_cmd([load_cfg_command])

            publish_command = (
                f'cd {found_1c} && webinst -publish -apache24 -wsdir Base -dir "c:\\apache\\htdocs\\Base" '
                f'-connstr "File="{link}";" -confpath "C:\\Apache24\\conf\\httpd.conf" && net stop '
                f'Apache2.4 && net start Apache2.4')
            input_cmd([publish_command])

        return "Служба Apache успешно установлена и запущена."
    except subprocess.CalledProcessError as e:
        return f"Произошла ошибка при установке или запуске службы Apache: {e}"
    except Exception as e:
        return f"Произошла неожиданная ошибка: {e}"


def extract_links(file_content):
    """Extracts all database paths from the given content."""
    return re.findall(r'Connect=File="(.+?)";', file_content)


def read_file_content(file_path):
    """Reads and returns the content of the specified file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def find_1c_base_list():
    appdata_path = os.getenv('APPDATA')

    file_path = os.path.join(appdata_path, '1C', '1CEStart', 'ibases.v8i')

    links_base = []

    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    content = read_file_content(file_path)
    links = extract_links(content)

    if links:
        for link in links:
            links_base.append(link)
        return links_base
    else:
        print("No links found.")


bases = find_1c_base_list()
if bases:
    print("Найденные базы 1С:")
    for base in bases:
        print(base)
else:
    print("Базы 1С не найдены.")