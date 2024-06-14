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
        input_cmd([f'cd {found_1c} && webinst -publish -apache24 -wsdir Base -dir "c:\\apache\\htdocs\\Base" -connstr "File=\\"{found_base}";" -confpath "C:\\Apache24\\conf\\httpd.conf"'])

        return "Служба Apache успешно установлена и запущена."
    except subprocess.CalledProcessError as e:
        return f"Произошла ошибка при установке или запуске службы Apache: {e}"
    except Exception as e:
        return f"Произошла неожиданная ошибка: {e}"


