from logic.installing_apache_and_file import copy_apache_and_exp
from logic.command_line_and_permissions import sub_run
from logic.exe_bit_extractor import exe_bit


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
