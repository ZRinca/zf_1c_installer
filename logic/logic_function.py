from logic.command_line_and_permissions import read_file_content, extract_bases, write_read_json
from logic.apache_install import copy_apache_and_exp, find_publication_apache
from logic.the_zf_plug import create_file_folder_zf, replace_text_in_xml
from logic.installing_file import move_and_rename_deskey_file
from settings import the_path_to_zf, the_path_to_Apache, the_path_to_Extension
from logic.command_line_and_permissions import sub_run
from logic.agent_mode import enter_commands_agent_mod
from Windows.window_error import show_error_window
from logic.search_1c import find_display_names
from logic.line_changer import insert_a_line
from logic.installing_file import copy_file
from logic.exe_bit_extractor import exe_bit
import os


def find_full_1c():
    find_1c = find_display_names(r'SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall')
    find_1c_2 = find_display_names(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')

    found_all_One_C = find_1c.copy()
    found_all_One_C.update(find_1c_2)
    return found_all_One_C


def find_1c_base_list(global_config):
    appdata_path = os.getenv('APPDATA')
    bases = {}

    if 'One_C' in global_config:
        one_c_user = global_config['One_C_the_user']
        one_c = global_config['One_C']

        if '\\1cv8\\' in one_c[one_c_user]:
            file = os.path.join(appdata_path, '1C', '1CEStart', 'ibases.v8i')
            bases = extract_bases(read_file_content(file))
        else:
            file = os.path.join(appdata_path, '1C', '1CEStartt', 'ibases.v8i')
            bases = extract_bases(read_file_content(file))
    else:
        file_patch = [os.path.join(appdata_path, '1C', '1CEStart', 'ibases.v8i'),
                      os.path.join(appdata_path, '1C', '1CEStartt', 'ibases.v8i')
                      ]

        for file in file_patch:
            bases.update(extract_bases(read_file_content(file)))

    if bases:
        return bases
    else:
        print('No bases found.')
        return {}


def install_extension(caller_window, global_config):
    one_c_user = global_config['One_C_the_user']
    one_c = global_config['One_C']

    cestart_t = None

    copy_file('extension', the_path_to_Extension)

    if '1cv8t' in one_c[one_c_user]:
        bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8t.exe')
    else:
        bit = exe_bit(f'{one_c[one_c_user]}\\bin\\1cv8.exe')

    if '1cv8t' in one_c[one_c_user]:
        cestart_t = r'C:\Program Files (x86)\1cv8t\common\1cestartt.exe'
    else:
        if bit == 32:
            cestart_t = r'C:\Program Files (x86)\1cv8\common\1cestart.exe'
        if bit == 64:
            cestart_t = r'C:\Program Files\1cv8\common\1cestart.exe'

    designer_command = [
        cestart_t,
        'DESIGNER',
        '/AgentMode',
        '/AgentBaseDir', the_path_to_Extension,
        '/IBName', global_config['base_the_One_C'],
        '/AgentSSHHostKeyAuto',
        '/Visible'
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

    if '1cv8t' in one_c[one_c_user]:
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

    i = 1

    if '1cv8t' in one_c[one_c_user]:
        webinst_t = 'webinstt'
    else:
        webinst_t = 'webinst'

    while True:
        if os.path.exists(f'C:\\1c_web\\Base_{i}'):
            i += 1
        else:
            break

    server_pub = ['-apache24', '-iis']
    publish = False

    for server in server_pub:
        publish = sub_run([
            f'{one_c[one_c_user]}\\bin\\{webinst_t}',
            '-publish',
            server,
            '-wsdir', f'Base_{i}',
            '-dir', f'c:\\1c_web\\Base_{i}',
            '-connstr', base[base_user],
            '-confpath', r'C:\Apache24\conf\httpd.conf'
        ])
        if 'Публикация выполнена' or 'Публикация обновлена' in publish.replace('\n', ''):
            publish = True
            print('Публикация выполненна')
            break

    if not publish:
        show_error_window('Публикация не выполненна!')
        caller_window.open_next_window()

    insert_a_line(f'c:\\1c_web\\Base_{i}\\default.vrd')

    print(sub_run(r'net stop Apache2.4'))
    print(sub_run(r'net start Apache2.4'))

    caller_window.open_next_window()


def install_zf(caller_window, global_config):
    copy_file('zf_1c_connect_client', the_path_to_zf)
    caller_window.open_next_window()


def loading_task(caller_window, global_config):
    link_url = find_publication_apache(global_config)
    path = create_file_folder_zf()

    write_read_json(f'{path[0]}\\settings.json', 'data_server_url', f'http://localhost{link_url}/')
    replace_text_in_xml(f'{path[0]}\\ZFConnector_settings.xml', 'REPLACETEXT', f'{path[0]}')
    replacement_text = f'Base_{path[1]}'

    move_and_rename_deskey_file(global_config['link_key'], 'source_key.dskey', 'C:\\zf_connector\\' + replacement_text)
    sub_run(f'SCHTASKS /Create /TN \\ZeroFactor\\{replacement_text} /XML {f'{path[0]}\\ZFConnector_settings.xml'}')
    sub_run(f'SCHTASKS /Run /TN \\ZeroFactor\\{replacement_text}')

    caller_window.open_next_window()
