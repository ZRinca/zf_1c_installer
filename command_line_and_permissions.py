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
        print(f'AAAAAA{found_base}')
        input_cmd([f'cd {found_1c} && webinst -publish -apache24 -wsdir Base -dir "c:\\apache\\htdocs\\Base" -connstr "File=\\"{found_base}";" -confpath "C:\\Apache24\\conf\\httpd.conf"'])
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
    file_path = r"C:\Users\admin\AppData\Roaming\1C\1CEStart\ibases.v8i"

    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    content = read_file_content(file_path)
    links = extract_links(content)

    if links:
        print("Found links:")
        for link in links:
            print(f"- {link}")
            return links
    else:
        print("No links found.")



