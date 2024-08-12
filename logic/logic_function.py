from Windows.window_error import show_error_window
from logic.command_line_and_permissions import read_file_content, extract_bases
from logic.installing_file import move_and_rename_deskey_file
from logic.command_line_and_permissions import sub_run
from logic.agent_mode import enter_commands_agent_mod
from logic.apache_install import copy_apache_and_exp
from logic.search_1c import find_display_names
from logic.line_changer import insert_a_line
from logic.installing_file import copy_file
from logic.exe_bit_extractor import exe_bit
from logic.the_zf_plug import create_file_folder_zf, replace_text_in_xml
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


def install_extension(caller_window, global_config):
    one_c_user = global_config['One_C_the_user']
    one_c = global_config['One_C']

    if "1cv8t" in one_c[one_c_user]:
        designer_command = [
            r"C:\Program Files (x86)\1cv8\common\1cestartt.exe",
            "DESIGNER",
            "/AgentMode",
            "/AgentBaseDir", r"C:\Apache24\Api",
            "/IBName", global_config['base_the_One_C'],
            "/AgentSSHHostKeyAuto",
            "/Visible"
        ]

        print(sub_run(designer_command))
    else:
        designer_command = [
            r"C:\Program Files\1cv8\common\1cestart.exe",
            "DESIGNER",
            "/AgentMode",
            "/AgentBaseDir", r"C:\Apache24\Api",
            "/IBName", global_config['base_the_One_C'],
            "/AgentSSHHostKeyAuto",
            "/Visible"
        ]

        print(sub_run(designer_command))
    to_back = enter_commands_agent_mod(global_config['LOGIN'], global_config['PASSWORD'])
    if to_back:
        caller_window.open_prev_window()
    else:
        caller_window.open_next_window()


def install_apache(caller_window, global_config):
    one_c_user = global_config['One_C_the_user']
    one_c = global_config['One_C']

    if "1cv8t" in one_c[one_c_user]:
        bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8t.exe')
    else:
        bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8.exe')
    copy_apache_and_exp(bit)

    output = sub_run(r'C:\Apache24\bin\httpd.exe -k install')
    if 'Service is already installed' in output:
        show_error_window('Apache уже установлен!')
        caller_window.open_next_window()
    else:
        print(sub_run(r'net stop Apache2.4'))
        print(sub_run(r'net start Apache2.4'))
        caller_window.open_next_window()


def publish_one_c(caller_window, global_config):

    one_c_user = global_config['One_C_the_user']
    one_c = global_config['One_C']

    base_user = global_config['base_the_One_C']
    base = global_config['base']

    if "1cv8t" in one_c[one_c_user]:
        webinst_command = [
            f"{one_c[one_c_user]}\\bin\\webinstt",
            "-publish",
            "-apache24",
            "-wsdir", "Base",
            "-dir", r"c:\apache\htdocs\Base",
            f"-connstr", base[base_user],
            "-confpath", r"C:\Apache24\conf\httpd.conf"
        ]
        print(sub_run(webinst_command))
    else:
        webinst_command = [
            f"{one_c[one_c_user]}\\bin\\webinst",
            "-publish",
            "-apache24",
            "-wsdir", "Base",
            "-dir", r"c:\apache\htdocs\Base",
            f"-connstr", base[base_user],
            "-confpath", r"C:\Apache24\conf\httpd.conf"
        ]
        print(webinst_command)
        print(sub_run(webinst_command))

        insert_a_line()

        print(sub_run(r'net stop Apache2.4'))
        print(sub_run(r'net start Apache2.4'))

        caller_window.open_next_window()


def install_zf(caller_window, global_config):
    copy_file('zf_1c_connect_client', the_path_to_zf)
    path = create_file_folder_zf()

    file_path = f'{path[0]}\\ZFConnector_settings.xml'
    target_text = 'REPLACETEXT'
    replacement_text = f'{path[0]}'

    replace_text_in_xml(file_path, target_text, replacement_text)

    target_text = 'REPLACETASKPLANNER'
    replacement_text = f'Base_{path[1]}'

    global_config['file_path_xml'] = file_path
    global_config['name_base_zf'] = replacement_text
    global_config['base_to_zf'] = 'C:\\zf_connector\\' + replacement_text

    replace_text_in_xml(file_path, target_text, replacement_text)

    caller_window.open_next_window()


def loading_task(caller_window, global_config):
    move_and_rename_deskey_file(global_config['link_key'], 'source_key.dskey', global_config['base_to_zf'])
    sub_run(f'SCHTASKS /Create /TN \\ZeroFactor\\{global_config['name_base_zf']} /XML {global_config['file_path_xml']}')
    sub_run(f'SCHTASKS /Run /TN \\ZeroFactor\\{global_config['name_base_zf']}')
    caller_window.open_next_window()
