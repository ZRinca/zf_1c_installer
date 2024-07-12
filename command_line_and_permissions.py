import os
import re
import subprocess
import ctypes
from agent_mode import enter_commands_agent_mod


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


def run_as_admin(found_1c, found_base, login, password):
    try:

        def sub_run(commands):
            p = subprocess.run(commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               encoding='CP866')
            if p.stderr == '':
                return p.stdout
            if p.stdout == '':
                return p.stderr
            else:
                return 'output is empty !'

        # Примеры команд

        print(sub_run(r'C:\Apache24\bin\httpd.exe -k install'))
        print(sub_run(r'net stop Apache2.4'))
        print(sub_run(r'net start Apache2.4'))

        webinst_command = [
            f"{found_1c}\\webinst",
            "-publish",
            "-apache24",
            "-wsdir", "Base",
            "-dir", r"c:\apache\htdocs\Base",
            f"-connstr", f'File="{found_base[list(found_base.keys())[0]]}";',
            "-confpath", r"C:\Apache24\conf\httpd.conf"
        ]

        print(sub_run(webinst_command))

        designer_command = [
            r"C:\Program Files\1cv8\common\1cestart.exe",
            "DESIGNER",
            "/AgentMode",
            "/AgentBaseDir", r"C:\Apache24\Api",
            "/IBName", list(found_base.keys())[0],
            "/AgentSSHHostKeyAuto",
            "/Visible"
        ]

        print(sub_run(designer_command))
        
        print(sub_run(r'net stop Apache2.4'))
        print(sub_run(r'net start Apache2.4'))

        # input_cmd(["cd C:\\Apache24\\bin && httpd.exe -k install && net start Apache2.4"])

        # load_cfg_command = f'cd {found_1c} && 1cv8 DESIGNER /F"{link}" /LoadCfg "C:\\Apache24\\Api\\InterfaceAPI.cfe" -Extension "InterfaceAPI"'
        # input_cmd([load_cfg_command])

        # if "Webinstt" in os.listdir(found_1c):
        #     time.sleep(5)
        #     publish_command = (
        #         f'cd {found_1c} && webinstt -publish -apache24 -wsdir Base -dir "c:\\apache\\htdocs\\Base" '
        #         f'-connstr "File="{found_base[list(found_base.keys())[0]]}";" -confpath "C:\\Apache24\\conf\\httpd.conf" && net stop '
        #         f'Apache2.4 && net start Apache2.4')
        #     input_cmd([publish_command])
        #     time.sleep(5)
        #     agent_1c_start = (
        #         f'cd {found_1c} && cd ../../common && 1cestartt.exe DESIGNER '
        #         f'/AgentMode /AgentBaseDir "C:\\Apache24\\Api" '
        #         f'/IBName "{list(found_base.keys())[0]}" '
        #         f'/AgentSSHHostKeyAuto /Visible'
        #     )
        #
        #     input_cmd([agent_1c_start])
        # else:
        #     time.sleep(5)
        #     publish_command = (
        #         f'cd {found_1c} && webinst -publish -apache24 -wsdir Base -dir "c:\\apache\\htdocs\\Base" '
        #         f'-connstr "File="{found_base[list(found_base.keys())[0]]}";" -confpath "C:\\Apache24\\conf\\httpd.conf" && net stop '
        #         f'Apache2.4 && net start Apache2.4')
        #     input_cmd([publish_command])
        #     time.sleep(5)
        #     agent_1c_start = (
        #         f'cd {found_1c} && cd ../../common && 1cestart.exe DESIGNER '
        #         f'/AgentMode /AgentBaseDir "C:\\Apache24\\Api" '
        #         f'/IBName "{list(found_base.keys())[0]}" '
        #         f'/AgentSSHHostKeyAuto /Visible'
        #     )
        #
        #     input_cmd([agent_1c_start])
        # time.sleep(15)
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
