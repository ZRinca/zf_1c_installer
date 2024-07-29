import re
import os
import winreg


def find_display_names(reg_path):

    write = {}

    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

        num_subkeys = winreg.QueryInfoKey(key)[0]

        for i in range(num_subkeys):
            try:

                subkey_name = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, subkey_name)

                display_name, _ = winreg.QueryValueEx(subkey, "DisplayName")
                install_source, _ = winreg.QueryValueEx(subkey, "InstallSource")
                install_location, _ = winreg.QueryValueEx(subkey, "InstallLocation")

                if os.path.exists(f'{install_location}\\bin\\1cv8.exe') or os.path.exists(f'{install_location}\\bin\\1cv8t.exe'):
                    if re.search(r"\b1cv8", install_location):
                        write[display_name] = install_location
                winreg.CloseKey(subkey)
            except WindowsError:
                continue

        winreg.CloseKey(key)
    except Exception as e:
        print("Ошибка при доступе к реестру:", e)
    return write

