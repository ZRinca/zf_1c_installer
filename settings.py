from logic.app_starter import base_path

"""Release settings"""
base_dir = base_path()

Apache_in_installer = {
    '32': f'{base_dir}\\Apache\\Apache_32\\Apache24',
    '64': f'{base_dir}/Apache/Apache_64/Apache24'
}

zf_connector_path = f'{base_dir}\\zf_1c_connect_client'
extension = f'{base_dir}\\extension'
output = f'{base_dir}\\output'
plink = f'{base_dir}\\PLINK.EXE'
version_info = f'{base_dir}\\version_info.rc'
ico_core = f'{base_dir}\\ico\\ZF_green.ico'

""" Mock VERSION """
# Apache_in_installer = {'32': 'Apache/Apache_32/Apache24', '64': 'Apache/Apache_64/Apache24'}
# zf_connector_path = 'zf_1c_connect_client'
# extension = 'extension'
# version_info = 'version_info.rc'
# plink = 'PLINK.EXE'
# output = 'output'
# ico_core = 'ico/ZF_green.ico'

"""In this file, you can change the path and other settings."""
the_path_to_zf = 'C:\\zf_connector\\'
the_path_to_Apache = 'C:\\Apache24'
the_path_to_Extension = 'C:\\zf_connector\\Extension'

"""here you can adjust the speed of the circle"""
loading_mug_speed = 5

"""Here you can change the font size"""
font_text = 'Rubik Light'
header_text_size = 16
body_text_size = 12
