from logic.command_line_and_permissions import sub_run
from logic.installing_file import copy_file
from logic.exe_bit_extractor import exe_bit
from settings import the_path_to_Apache


def copy_apache_and_exp(bit):
    source_dir = None
    if bit == 32:
        source_dir = r'Apache/Apache_32/Apache24'
    if bit == 64:
        source_dir = r'Apache/Apache_64/Apache24'
    copy_file(source_dir, the_path_to_Apache)
    copy_file('extension', f"{the_path_to_Apache}\\Api")
    return


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
