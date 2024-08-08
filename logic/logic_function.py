from logic.command_line_and_permissions import read_file_content, extract_bases
from logic.command_line_and_permissions import sub_run
from logic.apache_install import copy_apache_and_exp
from logic.search_1c import find_display_names
from logic.installing_file import copy_file
from logic.exe_bit_extractor import exe_bit
from settings import the_path_to_zf
import os


def find_full_1c():
    find_1c = find_display_names(r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall")
    find_1c_2 = find_display_names(r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    found_all_One_C = find_1c.copy()
    found_all_One_C.update(find_1c_2)
    return found_all_One_C


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


def install_apache(caller_window, global_config):
    one_c_user = global_config['One_C_the_user']
    one_c = global_config['One_C']

    if "1cv8t" in one_c[one_c_user]:
        bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8t.exe')
    else:
        bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8.exe')
    copy_apache_and_exp(bit)

    print(sub_run(r'C:\Apache24\bin\httpd.exe -k install'))
    print(sub_run(r'net stop Apache2.4'))
    print(sub_run(r'net start Apache2.4'))
    caller_window.open_next_window()


def install_zf(caller_window, global_config):
    copy_file('zf_1c_connect_client', the_path_to_zf)
    sub_run(r'SCHTASKS /Create /TN \ZeroFactor\ZFConnector /XML C:\Apache24\Api\ZFConnector_settings.xml')
    caller_window.open_next_window()


def publish_one_c(caller_window, global_config):
